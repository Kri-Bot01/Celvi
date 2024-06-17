from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm,UserCreationForm
from django.contrib.auth.models import User
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from .tokens import account_activation_token 
from django.http import HttpResponse

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def activate(request, uidb64, token):  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')  

def signup(request): 
    form = CustomUserCreationForm(request.POST) 
    if form.is_valid(): 
        form.save() 
        username = form.cleaned_data.get('username') 
        password = form.cleaned_data.get('password') 
        email = form.cleaned_data.get('email')
        user = User.authenticate(username=username, password=password, email=email) 
        login(request, user) 
        return redirect('home') 
    context = { 
        'form': form 
    } 
    return render(request, 'registration/signup.html', context) 

