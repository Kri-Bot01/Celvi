from django.shortcuts import render
from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingForm
from .models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib import messages
from core.models import Product, Profile
import datetime

# Import Some Paypal Stuff
from django.urls import reverse
from django.conf import settings
import uuid # unique user id for duplictate orders

# Create your views here.
def payment_success(request):
    return render(request, "payment/payment_success.html", {})

def checkout(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()

    if request.user.is_authenticated:
        # Checkout as logged in user
        try:
            # Shipping User
            shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
            # Shipping Form
            shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        except ShippingAddress.DoesNotExist:
            # If no shipping address exists, create a new form
            shipping_form = ShippingForm(request.POST or None)
        return render(request, "payment/checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form })
    else:
        # Checkout as guest
        shipping_form = ShippingForm(request.POST or None)
        return render(request, "payment/checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})