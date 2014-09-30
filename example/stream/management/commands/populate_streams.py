import datetime
import random

from django.core.management.base import BaseCommand
from django.utils import timezone

from ... import models


BASE_TIME = timezone.now() - datetime.timedelta(days=90)
MAX_DAYS_AFTER_BASE = 10000
POINT_COUNT = 100000
STREAM_COUNT = 100


class Command(BaseCommand):
    def point_factory(self, stream):
        def create_point(scalar):
            point = models.Point()

            if scalar % 3:
                point.content = {'ignore': True}
            elif scalar % 7:
                point.content = {'important': True}
            else:
                point.content = {'important': False, 'ignore': False}

            point.time_created = BASE_TIME + datetime.timedelta(
                days=int(random.random() * MAX_DAYS_AFTER_BASE)
            )

            point.stream = stream
            point.save()

            return point

        return create_point

    def create_stream(self, pk):
        stream = models.Stream.objects.create(
            pk=pk,
            name='Example Stream #' + str(pk),
        )

        stream.points = map(self.point_factory(stream), range(1, POINT_COUNT))
        stream.save()

        return stream

    def handle(self, *args, **kwargs):
        # Delete all Points and Streams
        for Model in [models.Point, models.Stream]:
            Model.objects.all().delete()

        map(self.create_stream, range(1, STREAM_COUNT))
