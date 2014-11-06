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

    class Meta(object):
        ordering = (
            'time_created',
        )

    content_string = models.TextField(_('related content'))
    time_created = models.DateTimeField(_('time created'))

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

    def __unicode__(self):
        return str(self.time_created)

    def save(self, *args, **kwargs):
        """ Override save instead of using `auto_now_add`.

        This is because `auto_now_add` will override explicitly assigned values
        on first save.

        """

        if not self.time_created:
            self.time_created = timezone.now()

        return super(Point, self).save(*args, **kwargs)
