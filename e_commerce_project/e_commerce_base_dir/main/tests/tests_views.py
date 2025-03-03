from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class TestingViews(TestCase):
    def test_main_page_loads_correctly(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
    
    def test_help_page_loads_correctly(self):
        response = self.client.get(reverse('help'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'help.html')
    
    def test_contact_page_loads_correctly(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')