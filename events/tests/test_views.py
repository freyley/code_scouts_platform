# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse

from django.test import TestCase
from django.conf import settings

from ..views import calendar_view

class CalendarViewTest(TestCase):

    def test_calendar_view(self):
        response = calendar_view("FakeRequest")
        self.assertContains(response, settings.CS_GOOGLE_CALENDAR,
            status_code=200)
        self.assertTemplateUsed(response, 'events/calendar.html')
