from django.core.management.base import BaseCommand
from blogapp.models import Author, Post
import datetime
from random import randint, choice


class Command(BaseCommand):
    help = 'Generate fake posts.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for author in Author.objects.all():
            for i in range(1, count + 1):
                post = Post(title=f'title_{i}',
                            description=f'description_{i}',
                            publish_date=f'{str(datetime.datetime.now())[:10]}',
                            author=author,
                            category=f'category_{i}',
                            views=f'{randint(1, 1000)}',
                            publish=f'{choice([True, False])}')
                post.save()
        self.stdout.write(f'{count} posts created!')
