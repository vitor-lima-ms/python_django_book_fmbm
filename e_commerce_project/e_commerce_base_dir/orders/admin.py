from django.contrib import admin
from .models import Orders, ItemOrdered

# Register your models here.

class ItemOrderedInline(admin.TabularInline):
    model = ItemOrdered
    raw_id_fields = ['product']

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'street',
        'house_number',
        'adress_complement',
        'neighborhood',
        'city',
        'state',
        'zip_code',
        'order_date',
        'paid'
    ]

    list_filter = ['paid', 'order_date', 'name']

    inlines = [ItemOrderedInline]