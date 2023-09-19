from django.core.management.base import BaseCommand
from blogapp.models import Author, Post
from datetime import datetime


class Command(BaseCommand):
    help = 'Create post.'

    def add_arguments(self, parser):
        parser.add_argument('author', type=int, help='Author ID')

    def handle(self, *args, **kwargs):
        author = Author.objects.get(pk=kwargs.get('author'))
        post = Post(title=f'title_N',
                    description=f'description_N',
                    publish_date=f'{str(datetime.now())[:10]}',
                    author=author,
                    category=f'category_N',
                    views=f'N',
                    publish=True)
        post.save()

        self.stdout.write(f'Post created! Post ID: {post.pk}')
