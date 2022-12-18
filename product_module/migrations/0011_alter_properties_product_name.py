# Generated by Django 4.0.5 on 2022-10-27 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0010_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='product_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_properties', to='product_module.product', verbose_name='نام محصول'),
        ),
    ]