from django.test import TestCase, RequestFactory
from ..views import login

class LoginViewTest(TestCase):


    def test_login_page_renders(self):
        self.request = RequestFactory().request()
        response = login(self.request)
        self.assertTemplateUsed(response, "code_scouts_platform/login.html")
        self.assertContains(response, "Persona", status_code=200)

