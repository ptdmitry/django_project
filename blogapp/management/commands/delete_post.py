from django.core.management.base import BaseCommand
from blogapp.models import Post


class Command(BaseCommand):
    help = 'Delete post by post ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Post ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        post = Post.objects.filter(pk=pk).first()
        post.delete()
        self.stdout.write(f'Post deleted! Post ID: {post.pk}')
