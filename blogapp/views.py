from django.views.generic import TemplateView, DetailView, CreateView
from .models import Author, Post, Comment
from . import forms
from django.http import HttpResponse


def author(request):
    res = Author.objects.all()
    return HttpResponse(res)


def post(request):
    res = Post.objects.all()
    return HttpResponse(res)


class AllPostsView(TemplateView):
    template_name = 'blogapp/posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author.objects.get(pk=self.kwargs['author_id'])
        posts = Post.objects.filter(author=author).all()
        context['posts'] = posts
        return context


class DetailPost(DetailView):
    model = Post
    template_name = 'blogapp/detail_post.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj


class AddAuthor(CreateView):
    model = Author
    template_name = 'blogapp/add_author.html'
    form_class = forms.AddAuthorForm


class AuthorPage(DetailView):
    model = Author
    template_name = 'blogapp/author_page.html'


class AddPost(CreateView):
    model = Post
    template_name = 'blogapp/add_post.html'
    form_class = forms.AddPostForm


class AddCommentView(CreateView):
    model = Comment
    template_name = 'blogapp/add_comment.html'
    form_class = forms.AddCommentForm
