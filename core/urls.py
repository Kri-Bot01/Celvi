from django.urls import path
from .views import home,aboutcompany,Product_view,privacycompany,contactcompany,product_quality,reviews_company,product_description

urlpatterns = [
    path('', home, name="homepage"),
    path('aboutus',aboutcompany,name="aboutpage"),
    path('products',Product_view,name='product'),
    path('privacypolicy',privacycompany,name='privacy'),
    path('contactus',contactcompany,name='contactpage'),
    path('productquality',product_quality,name='qualitypage'),
    path('reviews',reviews_company,name='reviewspage'),
    path('product/<int:pk>',product_description,name='productdescr'),
]