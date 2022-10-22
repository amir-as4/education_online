from django.db import models

# Create your models here.
from django_softdelete.models import SoftDeleteModel


class Article(SoftDeleteModel):
    title = models.CharField(max_length=100)
