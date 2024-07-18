from django.contrib import admin
from .models import Product, Product_type, Product_size, Product_gender, Profile
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Product)
admin.site.register(Product_type)
admin.site.register(Product_gender)
admin.site.register(Product_size)
admin.site.register(Profile)


class ProfileInline(admin.StackedInline):
    model = Profile


# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ("username", "first_name", "last_name", "email")
    inlines = [ProfileInline]


# Unregister the old way
admin.site.unregister(User)

# Re-Register the new way
admin.site.register(User, UserAdmin)