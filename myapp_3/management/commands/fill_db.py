from random import choices
from django.core.management.base import BaseCommand
from myapp_3.models import Author, Post

LOREM = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
'A dolores ducimus illo perferendis possimus sint sunt tenetur.'
'Culpa distinctio enim labore nihil nostrum quia voluptatibus!'
'Est hic itaque optio quam. Lorem ipsum dolor sit amet,'
'consectetur adipisicing elit. A dolores ducimus illo perferendis'
'possimus sint sunt tenetur. Culpa distinctio enim labore nihil'
'nostrum quia voluptatibus! Est hic itaque optio quam.'


class Command(BaseCommand):
    help = 'Generate fake authors and posts'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f'mail_{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title_{j}',
                    content=' '.join(choices(text, k=64)),
                    author=author
                )
                post.save()
