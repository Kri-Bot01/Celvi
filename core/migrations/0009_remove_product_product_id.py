# Generated by Django 5.0.6 on 2024-07-07 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_product_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_id',
        ),
    ]