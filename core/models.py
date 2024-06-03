from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_subname = models.CharField(max_length=200,null=True)
    product_type = models.ForeignKey("Product_type", on_delete=models.CASCADE)
    mrp = models.DecimalField(max_digits=8, decimal_places=2)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    product_description = models.TextField(blank = True)
    product_image = models.CharField(max_length=255)
    product_size = models.ForeignKey("Product_size", on_delete=models.CASCADE)
    product_color = models.CharField(max_length=25)
    product_gender = models.ForeignKey("Product_gender", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.product_name}_{self.product_color}_{self.id}"


class Product_type(models.Model):
    product_type_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.product_type_name}"

class Product_size(models.Model):
    product_size_name = models.CharField(max_length=5)
    product_size_desc = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.product_size_name}"

class Product_gender(models.Model):
    product_gender_name = models.CharField(max_length=1)
    product_gender_desc = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.product_gender_name}"