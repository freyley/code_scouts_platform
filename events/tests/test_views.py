# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse

from django.test import TestCase
from django.conf import settings

class CalendarViewTest(TestCase):

    def test_calendar_view(self):
        view = self.client.get(reverse('events:calendar'))
        self.assertContains(view, 'Calendar', status_code=200)
        self.assertContains(view, settings.CS_GOOGLE_CALENDAR)

    def test_calendar_template(self):
        view = self.client.get(reverse('events:calendar'))
        self.assertTemplateUsed(view, 'events/calendar.html')
