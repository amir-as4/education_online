from django.shortcuts import render, redirect
from django.urls import reverse
from product_module.models import ProductCategory
from .forms import ContactUsForm, ContactUsModelForm
from .models import ContactUs


# Create your views here.
# Receiving and validating and storing contact form information


def contact_us_page(request):
    if request.method == 'POST':
        # contact_form = ContactUsForm(request.POST)
        contact_form = ContactUsModelForm(request.POST)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            # contact = ContactUs(
            #     title=contact_form.cleaned_data.get('full_name'),
            #     full_name=contact_form.cleaned_data.get('full_name'),
            #     email=contact_form.cleaned_data.get('email'),
            #     number=contact_form.cleaned_data.get('phone'),
            #     message=contact_form.cleaned_data.get('message')
            # )
            # contact.save()
            contact_form.save()
            return redirect('index')
    else:
        contact_form = ContactUsModelForm()
    category = ProductCategory.objects.all()[:6]
    return render(request, 'contact_module/contact_us_page.html', {
        'categories': category,
        'contact_from': contact_form
    })
