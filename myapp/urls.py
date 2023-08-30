from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main'),
    path('about/', views.AboutPageView.as_view(), name='about'),
]
