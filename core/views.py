from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

def aboutcompany(request):
    return render(request, 'about.html')


class Product_view(ListView):
    model = Product
    template_name = 'products.html'

def privacycompany(request):
    return render(request, 'privacypolicy.html')

def contactcompany(request):
    return render(request, 'contact.html')

def product_quality(request):
    return render(request, 'product_quality.html')

def reviews_company(request):
    return render(request, 'reviews.html')

def product_description(request):
    return render(request, 'product_desc.html')
