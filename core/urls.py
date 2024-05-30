from django.urls import path
from .views import home,aboutcompany,productscompany

urlpatterns = [
    path('', home, name="homepage"),
    path('aboutus',aboutcompany,name="aboutpage"),
    path('products',productscompany,name='product'),
]