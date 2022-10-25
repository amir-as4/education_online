from django.contrib import admin
from . import models


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_filter = ['category', 'is_active']
    list_display = ['title', 'price', 'is_active', 'is_delete']
    list_editable = ['price', 'is_active']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Parent)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductTag)
admin.site.register(models.Brand)
admin.site.register(models.ProductImage)
admin.site.register(models.Product_rates)
admin.site.register(models.Comment)
admin.site.register(models.Attributes)
admin.site.register(models.Properties)
