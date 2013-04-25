from django.contrib.auth import REDIRECT_FIELD_NAME
from django.test import TestCase, RequestFactory
from code_scouts_platform.views import login

class LoginViewTest(TestCase):


    def test_login_page_renders(self):
        self.request = RequestFactory().request()
        response = login(self.request)
        self.assertTemplateUsed(response, "code_scouts_platform/login.html")
        self.assertContains(response, "Persona", status_code=200)


    def test_login_page_includes_redirect_target(self):
        redirect_to = '/redirect_to_here'
        self.request = RequestFactory().get('/login',
            {REDIRECT_FIELD_NAME: redirect_to})
        response = login(self.request)
        self.assertContains(response, redirect_to)


    def test_offsite_redirects_disallowed(self):
        # The framework ought to make sure the auth mechanism doesn't allow
        # people to craft URLs that will send users to arbitrary places
        # through our site, but there's a hole:
        # https://github.com/omab/django-social-auth/issues/676
        # so we'll do this check ourselves.
        redirect_to = 'http://example.com/hackme'
        self.request = RequestFactory().get('/login',
            {REDIRECT_FIELD_NAME: redirect_to})
        response = login(self.request)
        self.assertNotContains(response, redirect_to)
        # FIXME: the logger that gets run here prints crappy
        #     "no handlers could be found" messages during the test run.
