from django import forms
from .models import Orders

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = [
        'name',
        'street',
        'house_number',
        'adress_complement',
        'neighborhood',
        'city',
        'state',
        'zip_code',
    ]