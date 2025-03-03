from django.views.generic.edit import FormView
from main import forms
from django.shortcuts import render, get_object_or_404
from main.models import Category, Product
from chart.forms import ShopChartForm

# Create your views here.

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = forms.ContactForm
    success_url = '/'
    
    def form_valid(self, form: forms.ContactForm):
        form.send_msg_to_mail()
        return super().form_valid(form)

def shown_products(request, category_slug: str=None):
    category = None
    category_list: list[Category] = Category.objects.all()
    product_list: list[Product] = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product_list = Product.objects.filter(category=category)
        
    context: dict = {
        'category': category,
        'category_list': category_list,
        'product_list': product_list
    }
    
    return render(request, 'products/list.html', context)

def product_details(request, product_id: int, product_slug: str):
    product = get_object_or_404(Product, id=product_id, slug=product_slug, available=True)

    add_product_form = ShopChartForm()

    context: dict = {
        'product': product,
        'form': add_product_form
    }

    return render(request, 'products/details.html', context)