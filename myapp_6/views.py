from django.shortcuts import render
from django.db.models import Sum
from myapp_5.models import Product


def total_in_db(request):
    """Представление для суммирования в БД."""
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Общее количество посчитано в базе данных.',
        'total': total,
    }
    return render(request, 'myapp_6/total_count.html', context)


def total_in_view(request):
    """Представление для суммирования в представлении."""
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Общее количество посчитано в представлении.',
        'total': total,
    }
    return render(request, 'myapp_6/total_count.html', context)


def total_in_template(request):
    """Представление для суммирования в модели из шаблона."""
    context = {
        'title': 'Общее количество посчитано в шаблоне.',
        'total': Product,
    }
    return render(request, 'myapp_6/total_count.html', context)
