from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory, ProductTag
from django.http import Http404
from django.db.models import Avg, Max, Min


# Create your views here.
def product_list(request):
    tag = ProductTag.objects.all()
    product = Product.objects.all().order_by('price')  # [:5]  # order_by('-price')
    category = ProductCategory.objects.all().order_by('title')
    return render(request, 'product_module/product_list.html', {
        'products': product,
        'categories': category,
        'tags': tag
    })


def product_detail(request, slug):
    # try:
    #     product = Product.objects.get(id=product_id)
    # except:
    #     raise Http404()
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_module/product_detail.html', {
        'product': product
    })
