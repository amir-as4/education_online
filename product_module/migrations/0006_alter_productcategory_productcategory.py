# Generated by Django 4.0.5 on 2022-10-23 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0005_parent_remove_productcategory_parent_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='productcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_to_children', to='product_module.parent', verbose_name='رابطه با والد'),
        ),
    ]
