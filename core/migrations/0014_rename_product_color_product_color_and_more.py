# Generated by Django 5.0.6 on 2024-07-08 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_product_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_color',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_size',
            new_name='size',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_subname',
            new_name='subname',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_type',
            new_name='type',
        ),
    ]