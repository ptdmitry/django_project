from django.db import models
from django.db.models import Manager
from django.urls import reverse


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    registered_date = models.DateField(auto_now_add=True)
    objects = Manager()

    def __str__(self):
        return f'Name client: {self.name}, email: {self.email}, registered_date: {self.registered_date}'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    objects = Manager()

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(default=999999.99, max_digits=8, decimal_places=2)
    count = models.PositiveSmallIntegerField(default=0)
    added_date = models.DateField(auto_now_add=True)
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)
    image = models.ImageField(upload_to='media/product_images',
                              default='default.png',
                              verbose_name='product_image')
    objects = Manager()

    def get_absolute_url(self):
        return reverse('myapp:product_page', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Product: {self.title}, price: {self.price}, added_date: {self.added_date}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    registered_order_date = models.DateField(auto_now_add=True)
    objects = Manager()

    def __str__(self):
        return (f'Client`s {self.client} order: {self.product},'
                f'amount: {self.amount},'
                f'registered_order_date: {self.registered_order_date}')
