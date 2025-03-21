from decimal import Decimal
from django.conf import settings
from main.models import Product
from django.shortcuts import get_object_or_404

class ShopChart():
    def __init__(self, request):
        self.__session = request.session
        chart = self.__session.get(settings.ID_SHOPPING_CHART)

        if not chart:
            chart = self.__session[settings.ID_SHOPPING_CHART] = {}
        
        self.__chart = chart
    
    def __save(self):
        self.__session[settings.ID_SHOPPING_CHART] = self.__chart
        self.__session.modified = True
    
    def add(self, product: Product, qtd: int=1, att_qtd: bool=False):
        product_id = str(product.id)

        if product_id not in self.__chart:
            self.__chart[product_id] = {
                'id': product_id,
                'qtd': 0,
                'price': str(product.price)
            }

        if att_qtd:
            self.__chart[product_id]['qtd'] = qtd
        else:
            self.__chart[product_id]['qtd'] += qtd

        product.stock -= qtd
        product.save()
        
        self.__save()

    def remove(self, product: Product):
        product_id = str(product.id)

        if product_id in self.__chart:
            product.stock += self.__chart[product_id]['qtd']
            product.save()
            del self.__chart[product_id]

        self.__save()
    
    def __iter__(self):
        products_ids = self.__chart.keys()
        products = Product.objects.filter(id__in=products_ids)
        chart = self.__chart.copy()

        for product in products:
            chart[str(product.id)]['product'] = product
        
        for item in chart.values():
            item['price'] = Decimal(item['price'])
            item['subtotal'] = Decimal(item['price']) * Decimal(item['qtd'])
            yield item
    
    def __len__(self):
        result = 0

        for item in self.__chart.values():
            result += item['qtd']
        
        return result
    
    def get_grand_total(self):
        result = Decimal(0.0)
        
        for item in self.__chart.values():
            subtotal = Decimal(item['qtd']) * Decimal(item['price'])
            result += subtotal
        
        return result

    def clean_charts(self, request):
        for item in self.__chart.values():
            product = get_object_or_404(Product, id=int(item['id']))
            product.stock += item['qtd']
            product.save()

        for key in list(request.session.keys()):
            del request.session[key]
        
        request.session.modified = True

    def buy_charts(self, request):
        # I add the items again so that I can remove them if the purchase is made
        for item in self.__chart.values():
            product = get_object_or_404(Product, id=int(item['id']))
            product.stock += item['qtd']
            product.save()
        
        for item in self.__chart.values():
            product = get_object_or_404(Product, id=int(item['id']))
            product.stock -= item['qtd']
            product.save()

        for key in list(request.session.keys()):
            del request.session[key]
        
        request.session.modified = True