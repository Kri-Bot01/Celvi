# Generated by Django 5.0.6 on 2024-07-07 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_product_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
    ]