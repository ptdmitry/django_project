import logging
from django.views.generic import TemplateView, DetailView
from datetime import datetime
from django.views.generic.dates import YearArchiveView, MonthArchiveView, WeekArchiveView, ArchiveIndexView
from myapp import models

logger = logging.getLogger(__name__)


class MainPageView(TemplateView):
    logger.info('index.html accessed!')
    template_name = 'myapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main'
        return context


class AboutPageView(TemplateView):
    logger.info('about.html accessed!')
    template_name = 'myapp/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About'
        return context


class ClientView(DetailView):
    model = models.Client
    template_name = 'myapp/client_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_date'] = datetime.now()
        return context


class AllProductsView(ArchiveIndexView):
    model = models.Order
    date_field = 'registered_order_date'
    template_name = 'myapp/client_products.html'
    allow_future = False
    week_format = '%U'
    year_format = '%Y'

    def get_context_data(self, **kwargs):
        client = models.Client.objects.get(pk=self.kwargs.get('pk'))
        orders = super().get_queryset().filter(client=client).prefetch_related('product')
        product = set(product for order in orders for product in order.product.values_list('title'))

        context = super().get_context_data(**kwargs)
        context['product'] = product
        context['client'] = client

        return context

    def get_queryset(self, **kwargs):
        orders = models.Order.objects.get_queryset().filter(client=self.kwargs.get('pk'))

        return orders


class AllYearProductsView(AllProductsView, YearArchiveView):
    pass


class AllMonthProductsView(AllProductsView, MonthArchiveView):
    pass


class AllWeekProductsView(AllProductsView, WeekArchiveView):
    pass


class ProductView(DetailView):
    model = models.Product
    template_name = 'myapp/product_page.html'
