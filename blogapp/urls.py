from django.urls import path
from blogapp import views

app_name = 'blogapp'

urlpatterns = [
    path('author/', views.author, name='author'),
    path('posts/<int:author_id>', views.AllPostsView.as_view(), name='posts'),
    path('post/<int:pk>', views.DetailPost.as_view(), name='post'),
    path('add_author/', views.AddAuthor.as_view(), name='add_author'),
    path('author_page/<int:pk>/', views.AuthorPage.as_view(), name='author_page'),
    path('post/add/', views.AddPost.as_view(), name='add_post'),
    path('comment/add/<int:pk>', views.AddCommentView.as_view(), name='add_comment'),
]
