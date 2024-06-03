from django.urls import path
from .views import home,aboutcompany,Product_view

urlpatterns = [
    path('', home, name="homepage"),
    path('aboutus',aboutcompany,name="aboutpage"),
    path('products',Product_view.as_view(),name='product'),
]