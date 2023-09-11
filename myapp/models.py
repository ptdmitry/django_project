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


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    added_date = models.DateField(auto_now_add=True)
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
