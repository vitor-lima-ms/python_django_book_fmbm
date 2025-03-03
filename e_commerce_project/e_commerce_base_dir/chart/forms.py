from django import forms

PRODUCT_QTD_OPT = []
for i in range(1, 51):
    PRODUCT_QTD_OPT.append((i, str(i)))

class ShopChartForm(forms.Form):
    qtd = forms.TypedChoiceField(choices=PRODUCT_QTD_OPT, coerce=int, label='Quantidade')
    att = forms.BooleanField(required=False, widget=forms.HiddenInput)