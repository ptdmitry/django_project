from django.db import models
from django.db.models import Manager
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    objects = Manager()

    def get_absolute_url(self):
        return reverse('blogapp:author_page', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.name} {self.email }'


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    publish = models.BooleanField(default=False)

    objects = Manager()

    def get_absolute_url(self):
        return reverse('blogapp:post', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title} {self.description} {self.author}'


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = Manager()

    def __str__(self):
        return f'Comment by {self.author.name()} on "{self.post} {self.author}'
