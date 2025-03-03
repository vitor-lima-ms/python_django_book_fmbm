from django.test import TestCase
from django.core import mail
from main.forms import ContactForm

class TestingForms(TestCase):
    def test_form_correctly_filled(self):
        form = ContactForm(
            {
                'name': 'Test name',
                'email': 'test@email.com',
                'msg': 'Test msg'
            }
        )
        self.assertTrue(form.is_valid())
    
        form.send_msg_to_mail()
        self.assertEqual(mail.outbox[0].subject, 'Recebemos uma mensagem!')
        
    def test_form_incorrectly_filled(self):
        form = ContactForm(
            {
                'name': 'Test name'
            }
        )
        self.assertFalse(form.is_valid())