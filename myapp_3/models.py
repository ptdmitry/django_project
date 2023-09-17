from django.db import models
from django.db.models import Manager


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    objects = Manager()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    objects = Manager()

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:12])}...'

    def __str__(self):
        return f'Title is {self.title}'
