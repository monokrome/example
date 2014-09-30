from django.conf.urls import patterns, url
from .views import StreamDetailView


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', StreamDetailView.as_view()),
)
