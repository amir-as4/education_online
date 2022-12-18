from django.shortcuts import render
from product_module.models import ProductCategory


# Create your views here.
def contact_us_page(request):
    category = ProductCategory.objects.all()[:6]
    return render(request, 'contact_module/contact_us_page.html', {
        'categories': category
    })
