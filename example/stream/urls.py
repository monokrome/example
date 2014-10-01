from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$',
        views.StreamListView.as_view(),
        name='stream-list'),

    url(r'^(?P<pk>\d+)/$',
        views.StreamDetailView.as_view(),
        name='stream-detail'),
)
