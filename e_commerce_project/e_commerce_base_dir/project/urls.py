"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('help/', TemplateView.as_view(template_name='help.html'), name='help'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('', include('chart.urls'), name='chart'),
    path('', include('orders.urls'), name='orders'),
    path('', include('main.urls'), name='main'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
