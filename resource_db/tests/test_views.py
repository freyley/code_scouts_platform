from django.test import TestCase
from resource_db.models import LearningResource
from resource_db.views import resource_list

class ResourceDBTest(TestCase):
    def setUp(self):
        LearningResource.objects.get_or_create(
                url='www.udacity.com', title='New Title', tags='web dev',
                description='Online web development course', cost='Free', content_format='online class')
        LearningResource.objects.get_or_create(
                url='www.udemy.com', title='Second Test Title', tags='python, web dev',
                description='Online Python course', cost='$12', content_format='lectures')
        self.response = resource_list("Fake Request")

    def test_resource_list(self):
        self.assertContains(self.response, 'New Title')
        self.assertContains(self.response, 'Second Test Title')

    def test_resource_db_view(self):
        self.assertContains(self.response, 'Resource List', status_code=200)

    def test_resource_db_template(self):
        self.assertTemplateUsed(self.response, 'resource_db/resources.html')
