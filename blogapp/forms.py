from django import forms
from .models import Author, Post, Comment


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'bio', 'birthday']


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'author', 'category', 'publish_date']


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

        widgets = {
            'post': forms.HiddenInput(),
            'comment_text': forms.Textarea(attrs={'class': 'formControl'})
        }
