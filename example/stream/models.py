from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

import json


class Stream(models.Model):
    """ Grouped stream of Point objects. """

    name = models.CharField(_('name'), max_length=16)

    def __unicode__(self):
        return self.name


class Point(models.Model):
    """ Specific point of interesting data. """

    content_string = models.TextField(_('related content'))
    time_created = models.DateTimeField(_('Begins'))

    stream = models.ForeignKey(Stream, related_name='points')

    @property
    def content(self):
        """ Return the content for this Point as an object. """

        return json.loads(self.content_string)

    @content.setter
    def content(self, value):
        """ Update the stored JSON string for this point's content. """

        self.content_string = json.dumps(value)
        return self.content_string

    def save(self, *args, **kwargs):
        """ Saves the object while updating the time created if it's null. """

        if self.time_created is None:
            self.time_created = timezone.now()

        return super(Point, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.time_created)
