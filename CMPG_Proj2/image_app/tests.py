from django.test import TestCase

# Create your tests here.

class URLTest(TestCase):
    def test_testIndexpage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
