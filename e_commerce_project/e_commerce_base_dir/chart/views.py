from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Product
from chart.chart import ShopChart
from chart.forms import ShopChartForm
from django import forms

# Create your views here.

@require_POST
def add_to_chart(request, product_id: int):
    chart: ShopChart = ShopChart(request)
    product: Product = get_object_or_404(Product, id=product_id)
    form: ShopChartForm = ShopChartForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data

        if data['qtd'] > product.stock:
            chart: ShopChart = ShopChart(request)
            product: Product = get_object_or_404(Product, id=product_id)
            form: ShopChartForm = ShopChartForm(request.POST)
            return render(request, 'products/details_stock_error.html', {
                'chart': chart,
                'product': product,
                'form': form,
                'msg': 'Quantidade adicionada maior que a quantidade em estoque!'
            })

        chart.add(product, qtd=data['qtd'], att_qtd=data['att'])

    return redirect('chart:chart_details')       

def remove_from_chart(request, product_id: int):
    chart: ShopChart = ShopChart(request)
    product: Product = get_object_or_404(Product, id=product_id)

    chart.remove(product)
        
    return redirect('chart:chart_details')

def see_chart(request):
    return redirect('chart:chart_details')

def chart_details_view(request):
    chart: ShopChart = ShopChart(request)

    for item in chart:
        item['shop_chart_form'] = ShopChartForm(initial={
            'qtd': item['qtd'],
            'att': True
        })
    
    return render(request, 'chart/details.html', {'chart': chart})

def clean_all_items(request):
    chart: ShopChart = ShopChart(request)
    chart.clean_charts(request)

    return redirect('chart:chart_details')