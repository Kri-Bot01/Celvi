from django.contrib import admin
from .models import Product,Product_type,Product_size,Product_gender
# Register your models here.

admin.site.register(Product)
admin.site.register(Product_type)
admin.site.register(Product_gender)
admin.site.register(Product_size)