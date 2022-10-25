from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('contact-us', views.contact_page, name='contact'),
    # path('site-header', views.site_header_page, name='site_header')
]
