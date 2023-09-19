from django.core.management.base import BaseCommand
from blogapp.models import Post


class Command(BaseCommand):
    help = 'Get posts.'

    def handle(self, *args, **kwargs):
        posts = Post.objects.all()
        self.stdout.write(f'{posts}')
