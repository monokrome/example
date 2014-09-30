from django.views.generic import DetailView

from . import models


class StreamDetailView(DetailView):
    template_name = 'stream.html'
    context_object_name = 'stream'

    queryset = models.Stream.objects.all()
