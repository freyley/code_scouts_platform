# -*- coding: utf-8 -*-
"""Unit tests for project urlconf."""

from unittest import TestCase
from django.core.urlresolvers import resolve

from .. import urls


class TestURLs(TestCase):
    def test_resourceList(self):
        # This is not ideal, since it requires our test for
        # code_scouts_platform.urls to know something internal to events.urls,
        # but I don't know how to test for "is dispatched to events.urls."
        import events.views
        match = resolve('/events/calendar', urls)
        self.assertEqual(match.func, events.views.CalendarView)
