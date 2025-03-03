from django.urls import path
from django.views.generic import TemplateView
from main import views

app_name = 'main'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('products/', views.shown_products, name='products'),
    path('products/<str:category_slug>/', views.shown_products, name='products_by_cat'),
    path('products/<int:product_id>/<str:product_slug>/', views.product_details, name='product_details'),
]
