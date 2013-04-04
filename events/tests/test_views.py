# -*- coding: utf-8 -*-
from django.contrib.auth.models import AnonymousUser, User

from django.test import TestCase, RequestFactory
from django.conf import settings

from ..views import calendar_view

class CalendarViewTest(TestCase):

    def setUp(self):
        self.request = RequestFactory().request()


    def test_cannot_view_without_login(self):
        self.request.user = AnonymousUser()
        response = calendar_view(self.request)
        # Response should *not* contain Calendar, should do Redirect.
        # assertRedirect doesn't work with RequestFactory
        self.assertNotContains(response, "Calendar", 302)
        self.assertEqual(response['Location'], "/accounts/login/?next=/")


    def test_calendar_view_with_login(self):
        self.request.user = User()
        response = calendar_view(self.request)
        self.assertContains(response, settings.CS_GOOGLE_CALENDAR,
            status_code=200)
        self.assertTemplateUsed(response, 'events/calendar.html')
