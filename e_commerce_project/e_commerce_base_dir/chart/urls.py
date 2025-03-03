from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'chart'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('chart/add/<int:product_id>/', views.add_to_chart, name='add_to_chart'),
    path('chart/remove/<int:product_id>/', views.remove_from_chart, name='remove_from_chart'),
    path('chart/see/', views.see_chart, name='see_chart'),
    path('chart/cleaned/', views.clean_all_items, name='clean_all_items'),
    path('chart/details/', views.chart_details_view, name='chart_details'),
]