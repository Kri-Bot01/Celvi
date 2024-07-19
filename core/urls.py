from django.urls import path
from .views import home,aboutcompany,Product_view,privacycompany,contactcompany,product_quality,reviews_company,product_description,update_user,update_password,update_info

urlpatterns = [
    path('', home, name="homepage"),
    path('aboutus',aboutcompany,name="aboutpage"),
    path('products',Product_view,name='product'),
    path('privacypolicy',privacycompany,name='privacy'),
    path('contactus',contactcompany,name='contactpage'),
    path('update_user',update_user,name='update_user'),
    path('update_password',update_password,name='update_password'),
    path('update_info',update_info,name='update_info'),
    path('productquality',product_quality,name='qualitypage'),
    path('reviews',reviews_company,name='reviewspage'),
    path('product/<int:pk>',product_description,name='productdescr'),
]