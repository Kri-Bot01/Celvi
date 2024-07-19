from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import Product
from django.contrib.auth.decorators import login_required
from accounts.forms import UpdateUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib import messages
# Create your views here.
from accounts.forms import UpdateUserForm, ChangePasswordForm, UserInfoForm
from core.models import Profile
from payment.models import ShippingAddress
from payment.forms import ShippingForm



def home(request):
    return render(request, 'home.html')

def aboutcompany(request):
    return render(request, 'about.html')

def product_description(request,pk):
	product = Product.objects.get(id=pk)
	return render(request, 'product_desc.html', {'product':product})

def Product_view(request):
	products = Product.objects.all()
	return render(request, 'products.html', {'products':products})


#class Product_view(ListView):
#   model = Product
#   template_name = 'products.html'

def privacycompany(request):
    return render(request, 'privacypolicy.html')

def contactcompany(request):
    return render(request, 'contact.html')

def product_quality(request):
    return render(request, 'product_quality.html')

def reviews_company(request):
    return render(request, 'reviews.html')

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form  = UpdateUserForm(request.POST or None,instance=current_user)
        if user_form.is_valid():
                user_form.save()
                login(request,current_user)
                messages.success(request,"User has been Updated!!")
        return render(request, 'update_user.html',{'user_form':user_form})
    else:
        messages.success(request,"You must be logged in to access that page!!")  
    return render(request, 'update_user.html')


def update_password(request):
	if request.user.is_authenticated:
		current_user = request.user
		# Did they fill out the form
		if request.method  == 'POST':
			form = ChangePasswordForm(current_user, request.POST)
			# Is the form valid
			if form.is_valid():
				form.save()
				messages.success(request, "Your Password Has Been Updated...")
				login(request, current_user)
				return redirect('update_user')
			else:
				for error in list(form.errors.values()):
					messages.error(request, error)
					return redirect('update_password')
		else:
			form = ChangePasswordForm(current_user)
			return render(request, "update_password.html", {'form':form})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def update_info(request):
	if request.user.is_authenticated:
		# Get Current User
		current_user = Profile.objects.get(user__id=request.user.id)
		# Get Current User's Shipping Info
		shipping_user = Profile.objects.get(user__id=request.user.id)
		
		# Get original User Form
		form = UserInfoForm(request.POST or None, instance=current_user)
		# Get User's Shipping Form
		shipping_form = ShippingForm(request.POST or None, instance=shipping_user)		
		if form.is_valid() or shipping_form.is_valid():
			form.save()
			shipping_form.save()
			messages.success(request,"User has been Updated!!")
		return render(request, "update_info.html", {'form':form, 'shipping_form':shipping_form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('home')


