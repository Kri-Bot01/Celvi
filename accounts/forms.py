from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
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
from core.models import Profile

class UserInfoForm(forms.ModelForm):
	phone = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}), required=False)
	address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 1'}), required=False)
	address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 2'}), required=False)
	city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), required=False)
	state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}), required=False)
	zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zipcode'}), required=False)
	country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}), required=False)

	class Meta:
		model = Profile
		fields = ('phone', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', )


class UpdateUserForm(UserChangeForm):
	# Hide Password stuff
	password = None
	# Get other fields
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), required=False)
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}), required=False)
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}), required=False)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def __init__(self, *args, **kwargs):
		super(UpdateUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'


class ChangePasswordForm(SetPasswordForm):
	class Meta:
		model = User
		fields = ['new_password1', 'new_password2']

	def __init__(self, *args, **kwargs):
		super(ChangePasswordForm, self).__init__(*args, **kwargs)

		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['new_password1'].label = ''
		self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['new_password2'].label = ''
		self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

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
            'placeholder':'Be creative,Really...creative.', 
            'maxlength': '16', 
            'minlength': '6', 
            }) 
        self.fields['email'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'@', 
            'name':'email', 
            'id':'email', 
            'type':'email', 
            'placeholder':'Yes, your email', 
            }) 
        self.fields['password1'].widget.attrs.update({ 
            'class': 'form-input',
            'pattern': '(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]+',
            'title': 'Password must contain at least one capital letter, one small letter, one number, and one special character', 
            'required':'', 
            'name':'password1', 
            'id':'password1', 
            'type':'password', 
            'placeholder':"Please don't make it '123456'", 
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
            'placeholder':'Just do whatever you did up there', 
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
        return user
        
   