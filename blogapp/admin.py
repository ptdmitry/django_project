from django.contrib import admin
from .models import Author, Post, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'birthday']
    ordering = ['name']
    list_filter = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по полю имени автора (name)'
    readonly_fields = ['email', 'birthday']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'publish', 'publish_date']
    ordering = ['publish_date']
    list_filter = ['author']
    search_fields = ['author']
    search_help_text = 'Поиск по полю имени автора (author)'
    readonly_fields = ['author', 'category', 'publish_date']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_date', 'modified_date']
    ordering = ['modified_date']
    list_filter = ['author', 'created_date', 'modified_date']
    search_fields = ['author']
    search_help_text = 'Поиск по полю имени автора (author)'
    readonly_fields = ['author', 'created_date', 'modified_date']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
