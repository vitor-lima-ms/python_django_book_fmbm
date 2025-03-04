from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'orders'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('order/create/', views.order_create, name='create'),
    path('order/complete/', views.order_create, name='complete'),
]
