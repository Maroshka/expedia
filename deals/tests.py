from django.test import TestCase
from django.core.urlresolvers import resolve
from deals.views import find_deal
from django.http import HttpRequest

class HomePageTest(TestCase):
    def test_root_url(self):
        found = resolve('/')
        self.assertEqual(found.func, find_deal)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = find_deal(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Expedia Offers</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
