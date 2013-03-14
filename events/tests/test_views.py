# -*- coding: utf-8 -*-

from django.test import TestCase

class CalendarViewTest(TestCase):
    def test_calendarView(self):
    	view = self.client.get('/events/calendar')
    	self.assertContains(view, 'Calendar', status_code=200)
