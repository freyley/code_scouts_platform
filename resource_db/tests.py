from django.test import TestCase
from resource_db.models import importFromCSV
from cStringIO import StringIO

class SimpleTest(TestCase):
    def test_importFromCSV(self):
        input_file = StringIO("""URL,Short Title,Part of larger resource?,tags,description,cost,Location (or online),Start date,End date,"Format (video, tutorial, book etc.)",Members who might start here
http://example.com,Example Title,No,"Some, Tags",example description,$99,Online,N/A,N/A,Webpage,
""")
        resources = importFromCSV(input_file)
        self.assertEqual(len(resources), 1)
        r = resources[0]
        self.assertEqual(r.url, 'http://example.com')
        self.assertEqual(r.title, 'Example Title')
        self.assertEqual(r.tags, 'Some, Tags')
        self.assertEqual(r.description, 'example description')
        self.assertEqual(r.cost, '$99')
        self.assertEqual(r.content_format, 'Webpage')
