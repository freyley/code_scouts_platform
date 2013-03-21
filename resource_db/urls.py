from django.conf.urls import patterns, url

from .views import resource_list

urlpatterns = patterns('',
    url('^$', resource_list)
)