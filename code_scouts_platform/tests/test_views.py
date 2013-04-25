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
