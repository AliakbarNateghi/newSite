from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from smtplib import SMTPException, SMTPAuthenticationError
from .models import pro, Order, OrderItem


def Cart(customer):
    try:
        cart = Order.objects.get(customer=customer, in_cart=True)
    except Order.DoesNotExist:
        cart = Order.objects.get(customer=customer)
        cart.save()
    return cart
