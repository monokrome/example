from django.views.generic import DetailView
from django.views.generic import ListView

from . import models


class StreamDetailView(DetailView):
    template_name = 'stream/detail.html'
    context_object_name = 'stream'

    queryset = models.Stream.objects.all()


class StreamListView(ListView):
    template_name = 'stream/list.html'
    context_object_name = 'streams'

    queryset = models.Stream.objects.all()
