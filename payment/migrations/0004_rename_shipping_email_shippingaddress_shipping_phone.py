# Generated by Django 5.0.6 on 2024-07-19 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='shipping_email',
            new_name='shipping_phone',
        ),
    ]
