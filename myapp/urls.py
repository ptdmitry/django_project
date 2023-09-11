from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('client/<int:pk>/', views.ClientView.as_view(), name='client'),
    path('product/<int:pk>/', views.ProductView.as_view(), name='product'),
    path('orders/year/<int:year>/<int:pk>/', views.AllYearProductsView.as_view(), name='orders_year'),
    path('orders/month/<int:year>/<int:month>/<int:pk>/', views.AllYearProductsView.as_view(), name='orders_month'),
    path('orders/week/<int:year>/<int:month>/<int:week>/<int:pk>/',
         views.AllYearProductsView.as_view(), name='orders_week'),
]
