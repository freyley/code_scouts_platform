from django.conf.urls import patterns, url

from .views import ResourceList

urlpatterns = patterns('',
    url('^$', ResourceList)
)