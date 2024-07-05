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
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['username'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'username', 
            'id':'username', 
            'type':'text', 
            'placeholder':'John Doe', 
            'maxlength': '16', 
            'minlength': '6', 
            }) 
        self.fields['email'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'@', 
            'name':'email', 
            'id':'email', 
            'type':'email', 
            'placeholder':'JohnDoe@mail.com', 
            }) 
        self.fields['password1'].widget.attrs.update({ 
            'class': 'form-input',
            'pattern': '(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]+',
            'title': 'Password must contain at least one capital letter, one small letter, one number, and one special character', 
            'required':'', 
            'name':'password1', 
            'id':'password1', 
            'type':'password', 
            'placeholder':'password', 
            'maxlength':'22',  
            'minlength':'8' 
            }) 
        self.fields['password2'].widget.attrs.update({ 
            'class': 'form-input',
            
            "title": "Password should be the same as entered above!", 
            'required':'required' if self.data.get('password1') else 'Wrong pass', 
            'name':'password2', 
            'id':'password2', 
            'type':'password', 
            'placeholder':'re-enter-password', 
            'maxlength':'22',  
            'minlength':'8' 
            }) 
 
 
    username = forms.CharField(max_length=20, label=False) 
    email = forms.EmailField(max_length=100) 
 
    class Meta:
        model = User
        fields = ( "username","email",'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.is_active = False  
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            mail_subject = 'Activation link for your celvi accout'  
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
        return render(request, 'registration/email_sent_success.html', context) 
        return user
        
   