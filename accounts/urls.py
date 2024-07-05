from django.urls import path
from . import views
from .views import SignUpView,activate,signup


urlpatterns = [
    #path("signup/", SignUpView.as_view(), name="signup"),
    path("signup/", signup, name="signup"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',activate, name='activate'),
    
]