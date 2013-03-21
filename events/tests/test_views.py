# -*- coding: utf-8 -*-

from django.test import TestCase


class CalendarViewTest(TestCase):
    def test_calendar_view(self):
        view = self.client.get('/events/calendar')
        self.assertContains(view, 'Calendar', status_code=200)

    def test_calendar_template(self):
        view = self.client.get('/events/calendar')
        self.assertTemplateUsed(view, 'events/calendar.html')
