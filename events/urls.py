# -*- coding: utf-8 -*-
"""urlconf for events.
"""

from django.conf.urls import patterns, url

from .views import calendar_view

urlpatterns = patterns('',
    url('^calendar$', calendar_view, name='calendar')
)
