from django.shortcuts import render, redirect
from .models import ItemOrdered
from .forms import OrdersForm
from chart.chart import ShopChart

# Create your views here.

def order_create(request):
    chart = ShopChart(request)

    if request.method == 'POST':
        form = OrdersForm(request.POST)

        if form.is_valid():
            order = form.save()
        
        for item in chart:
            ItemOrdered.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                qtd=item['qtd']
            )
        
        chart.buy_charts(request)

        return render(request, 'orders/complete.html', {'order': order})
    
    else:
        form = OrdersForm()

        return render(request, 'orders/create.html', {'chart': chart, 'form': form})