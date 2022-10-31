from django.db import models
from django.urls import reverse
from account_module.models import User

# from django.utils.text import slugify

# Create your models here.
from django_softdelete.models import SoftDeleteModel


class Parent(models.Model):
    name = models.CharField(max_length=100, verbose_name='والد')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'والد'
        verbose_name_plural = 'والد'


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name="عنوان")
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در آدرس', unique=True)
    productcategory = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='parent_to_children', null=True,
                                        verbose_name='رابطه با والد')
    description = models.TextField(db_index=True, verbose_name='توضیحات اصلی')
    is_active = models.BooleanField(verbose_name='فعال/غیر فعال')
    is_delete = models.BooleanField(verbose_name='حذف شده/نشده')

    def __str__(self):
        return f'({self.title}-{self.url_title}-{self.description}-{self.is_active})'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Brand(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='نام')
    slug = models.CharField(max_length=150, db_index=True, unique=True, null=True, verbose_name='اسلاگ')
    is_active = models.BooleanField(default=1, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return f"({self.name}-{self.slug}-{self.is_active})"

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'


class Product(models.Model):
    title = models.CharField(max_length=500, verbose_name='نام محصول')
    category = models.ManyToManyField(ProductCategory, related_name='products_categories', verbose_name='دسته بندی ها')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='برند', null=True, blank=True)
    price = models.IntegerField(verbose_name='قیمت')
    duration = models.CharField(max_length=50, verbose_name='مدت ویدئو', null=True)
    short_description = models.CharField(max_length=650, null=True, db_index=True, verbose_name='توضیحات خلاصه')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True)
    primary_image = models.CharField(max_length=300, db_index=True, verbose_name='تصویر اصلی')
    status = models.IntegerField(default=1, verbose_name='وضعیت')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, verbose_name='عنوان در url',
                            max_length=200, unique=True)
    is_delete = models.BooleanField(verbose_name='حذف شده/نشده')

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"({self.title}-{self.price}-{self.short_description}-{self.description}-{self.primary_image}" \
               f"-{self.status})"

    class Meta:
        verbose_name = 'محصول '
        verbose_name_plural = 'محصولات'


class Properties(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام استاد')
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_properties', null=True,
                                     verbose_name='نام محصول')
    pic = models.CharField(max_length=300, verbose_name='تصویر مدرس')
    type = models.CharField(max_length=100, db_index=True, verbose_name='نوع')
    count = models.CharField(max_length=50, verbose_name='تعداد ویدئوها')

    def __str__(self):
        return f"({self.name}-{self.pic}-{self.type}-{self.count})"

    class Meta:
        verbose_name = 'متغیر'
        verbose_name_plural = 'متغیر ها'


class ProductImage(models.Model):
    image = models.CharField(max_length=100, db_index=True, verbose_name='تصویر')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')

    def __str__(self):
        return f"({self.image}-{self.product_id})"

    class Meta:
        verbose_name = 'تصویر '
        verbose_name_plural = 'تصاویر'


class ProductTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tag', verbose_name='محصول')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_comment')
    approved = models.BooleanField(default=1, verbose_name='تایید/عدم تایید')
    text = models.CharField(max_length=800, verbose_name='کامنت', db_index=True)

    def __str__(self):
        return f"({self.user_id}-{self.product_id}-{self.approved}-{self.text})"

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'


class Product_rates(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rate')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_rate')
    rate = models.IntegerField(verbose_name='امتیاز')

    def __str__(self):
        return f"({self.user_id}-{self.product_id}-{self.rate})"

    class Meta:
        verbose_name = 'امتیاز'
        verbose_name_plural = 'امتیاز ها'


class Attributes(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='ویژگی ها')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ویژگی'
        verbose_name_plural = 'ویژگی ها'
