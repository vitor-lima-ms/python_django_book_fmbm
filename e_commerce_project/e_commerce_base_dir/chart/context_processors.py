from .chart import ShopChart

def charts(request):
    result = {
        'chart': ShopChart(request)
    }

    return result