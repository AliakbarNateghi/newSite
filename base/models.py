from django.db import models
from django.contrib.auth.models import User


class pro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField(null=True)
    kind = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    available = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def availability(self):
        if self.available:
            return True
        else:
            return False

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['available']


class Order(models.Model):
    customer = models.ForeignKey(User, null=True,
                                 on_delete=models.CASCADE,
                                 related_name='orders')
    timestamp = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    in_cart = models.BooleanField(default=True)
    placed = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Order #{self.id} by {self.customer.first_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=True,
                              on_delete=models.CASCADE,
                              related_name='items')
    name = models.CharField(max_length=30, null=True)
    kind = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.order
