from django.shortcuts import render, get_object_or_404
from .cart import Cart
from core.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    return render(request, "cart.html")

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product)

        cart_quantity = cart.__len__()
        #response = JsonResponse({'Product Name: ': product.product_name})
        response = JsonResponse({'qty: ': cart_quantity})
        return response


def cart_delete(request):
    pass

def cart_update(request):
    pass