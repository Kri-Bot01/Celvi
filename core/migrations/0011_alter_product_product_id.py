# Generated by Django 5.0.6 on 2024-07-07 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.DecimalField(decimal_places=0, max_digits=8),
        ),
    ]
