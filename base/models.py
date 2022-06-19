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
