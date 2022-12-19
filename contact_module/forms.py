from django import forms
from .models import ContactUs

# Validate our contact form
from django.core import validators


class ContactUsForm(forms.Form):
    full_name = forms.CharField(label='نام و نام خانوادگی', max_length=50,
                                error_messages={'required': 'نام و نام خانوادگی الزامی است',
                                                'max_length': 'حداکثر 50 کاراکتر'},
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'نام و نام خانوادگی'
                                }))
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'ایمیل'
    }),
                             validators=[
                                 validators.EmailValidator
                             ])
    number = forms.IntegerField(label='شماره تماس', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'شماره تماس'
    }))
    message = forms.CharField(label='متن پیام', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'نوشتن پیام',
        'rows': ' 4'
    }))


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['title', 'full_name', 'email', 'number', 'message']
        # برای نشان دادن همه فیلدها
        # fields='__all__'
        # برای نشان دادن همه فیلدها بجز
        # exclude=['response']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control alert alert-success',
                'placeholder': 'نام و نام خانوادگی'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل'
            }),
            'number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'شماره تماس'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان'
            }),
            'message': forms.Textarea(attrs={
                'max_length': 'حداقل باید 50 کاراکتر باشد',
                'class': 'form-control',
                'placeholder': 'نوشتن پیام',
                'rows': '4'
            })
        }
        error_messages = {
            'full_name': {
                'required': 'این فیلد الزامی می باشد'
            },
            'email': {
                'required': 'این فیلد الزامی می باشد'
            },
            'number': {
                'required': 'این فیلد الزامی می باشد'
            },
            'title': {
                'required': 'این فیلد الزامی می باشد'
            },
            'message': {
                'required': 'این فیلد الزامی می باشد'
            }
        }
