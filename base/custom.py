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


def update_total(order):
    """
        Updates total price of order.
    """
    if not isinstance(order, Order):
        raise Http404("{} is not an instance of Order.".format(order))
    else:
        items = order.items.all()
        order.total = 0
        for item in items:
            order.total += item.price
        order.save()


def cart_count():
    pass
