from django.core.management.base import BaseCommand
from myapp_2.models import Author, Post


class Command(BaseCommand):
    help = 'Generate fake authors and posts.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Name_{i}', email=f'mail_{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title_{j}',
                    content=f'Text from {author.name} #{j} is bla bla bla many long text',
                    author=author
                )
                post.save()
