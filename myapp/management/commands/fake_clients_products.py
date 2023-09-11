from django.core.management.base import BaseCommand
from myapp.models import Client, Product
from random import randint
from datetime import datetime


class Command(BaseCommand):
    help = 'Generate fake clients and products.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Clients')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Name_{i}', email=f'mail_{i}@mail.ru',
                            phone=f'Phone_{i}', address=f'Addres_{i}',
                            registered_date=str(datetime.now()))
            client.save()
            for j in range(1, randint(1, 10)):
                product = Product(title=f'Title_{j}', description=f'Description_{j}',
                                  price=randint(100, 10_000),
                                  count=randint(1, 100),
                                  added_date=str(datetime.now()))
                product.save()
        self.stdout.write(f'{count} clients created!')
