from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def aboutcompany(request):
    return render(request, 'about.html')
def productscompany(request):
    return render(request, 'products.html')