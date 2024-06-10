from django.urls import path
from .views import home,aboutcompany,Product_view,privacycompany,contactcompany

urlpatterns = [
    path('', home, name="homepage"),
    path('aboutus',aboutcompany,name="aboutpage"),
    path('products',Product_view.as_view(),name='product'),
    path('privacypolicy',privacycompany,name='privacy'),
    path('contactus',contactcompany,name='contactpage')
]