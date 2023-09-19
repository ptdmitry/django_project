from django.core.management.base import BaseCommand
from blogapp.models import Post


class Command(BaseCommand):
    help = 'Get post by ID author.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        self.stdout.write(f'{post}')
