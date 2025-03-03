from django.contrib import admin
from main.models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'price',
        'stock',
        'available',
        'creation_date',
        'last_update_date',
    ]
    list_filter = [
        'available',
        'creation_date',
        'last_update_date',
    ]
    list_editable = [
        'price',
        'stock',
        'available',
    ]
    prepopulated_fields = {'slug': ('name',)}