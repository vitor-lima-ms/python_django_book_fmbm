from django.db import models
from decimal import Decimal
from main.models import Product

# Create your models here.

class Orders(models.Model):
    # Buyer data
    name = models.CharField(max_length=50)
    email = models.EmailField()
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=5)
    adress_complement = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=10)

    # Order data
    order_date = models.DateField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
            ordering = ('-order_date',)

    def __str__(self):
        return f'Order #{self.id}'
    
    def get_grand_total(self):
        result = Decimal(0.0)

        for item in self.items.all():
            subtotal = Decimal(item['qtd']) * Decimal(item['price'])
            result += subtotal
        
        return result

class ItemOrdered(models.Model):
    order = models.ForeignKey(Orders, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qtd = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Order #{self.id}'
    
    def get_subtotal(self):
         return self.price * self.qtd