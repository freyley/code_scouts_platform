# -*- coding: utf-8 -*-
"""urlconf for events.
"""

from django.conf.urls import patterns, url

from .views import CalendarView

urlpatterns = patterns('',
    url('^calendar$', CalendarView)
)
