from django.shortcuts import render

# Create your views here.
from product_module.models import ProductCategory


def site_header_component(request):
    return render(request, 'shared/site_header_component.html', {})


def site_footer_component(request):
    category = ProductCategory.objects.all()[:6]
    return render(request, 'shared/site_footer_component.html', {
        'categories': category
    })


def index_page(request):
    return render(request, 'home_module/index_page.html')


def contact_page(request):
    return render(request, 'home_module/contact_page.html')
