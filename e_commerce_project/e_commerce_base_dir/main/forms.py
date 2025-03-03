from django import forms
from django.core.mail import send_mail
from project import settings

class ContactForm(forms.Form):
    name = forms.CharField(required=True, label="Nome", initial="Digite seu nome")
    email = forms.EmailField(required=True, label="E-mail", initial="Digite seu e-mail")
    msg = forms.CharField(required=True, label="Mensagem", initial="Mensagem", widget=forms.Textarea)

    def send_msg_to_mail(self):
        send_mail(
           'Recebemos uma mensagem!',
            self.data['msg'],
            self.data['email'],
            [settings.EMAIL_HOST_USER],
            fail_silently=False
        )