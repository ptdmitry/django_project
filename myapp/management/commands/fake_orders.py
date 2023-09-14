from django.core.management.base import BaseCommand
from myapp.models import Client, Product, Order
from random import randint
from datetime import datetime


class Command(BaseCommand):
    help = 'Generate fake orders.'

    def add_arguments(self, parser):
        parser.add_argument('client', type=int, help='Client ID')
        # parser.add_argument('product', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        client = Client.objects.get(pk=kwargs.get('client'))
        order = Order(client=client, amount=randint(1_000, 100_000),
                      registered_order_date=datetime.now())

        order.save()
        for i in range(1, 10):
            product = Product.objects.get(pk=randint(1, 20))
            order.product.add(product)

        self.stdout.write(f'Orders created!')
