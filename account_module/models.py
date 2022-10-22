from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    mobile = models.CharField(max_length=20, verbose_name='شماره تماس')
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')
    avatar = models.CharField(max_length=50, verbose_name='آواتار')
    status = models.IntegerField(default=1, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()
