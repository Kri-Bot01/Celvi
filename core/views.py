from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

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