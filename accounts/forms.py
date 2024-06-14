from django.contrib.auth.forms import UserCreationForm
#import forms django
from django import forms
#import user model from django authapp
from django.contrib.auth.models import User
from .emailer import signup_success_email
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token 
from django.core.mail import send_mail
from django.conf import settings
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label = "Email")


    class Meta:
        model = User
        fields = ( "username","email",'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.is_active = False  
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('acc_active_email.html', {  
                'user': user,  
                'domain': "http://127.0.0.1:8000",  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            send_mail(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
        return user