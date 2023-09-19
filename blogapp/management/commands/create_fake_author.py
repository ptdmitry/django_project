from django.core.management.base import BaseCommand
from blogapp.models import Author
import datetime


class Command(BaseCommand):
    help = 'Generate fake authors.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'name_{i}',
                            email=f'mail_{i}@mail.ru',
                            bio=f'Bla bla bla {i}',
                            birthday=f'{str(datetime.datetime.now())[:10]}')
            author.save()
        self.stdout.write(f'{count} authors created!')
