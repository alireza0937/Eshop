import datetime

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from account.models import User


class ProductBrand(models.Model):
    title = models.CharField(max_length=300, db_index=True)
    url_title = models.CharField(max_length=300, db_index=True, default='url_title')
    is_active = models.BooleanField()

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField()

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300)
    category = models.ManyToManyField(ProductCategory)
    image = models.ImageField(null=True, upload_to='images/products', blank=True)
    price = models.CharField(max_length=100)
    brand = models.ForeignKey(ProductBrand, null=True, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=500, null=True, db_index=True)
    description = models.TextField(db_index=True)
    amount = models.IntegerField(default=0)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", null=False, db_index=True, editable=False, max_length=200, unique=True)
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField()
    is_new = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductTags(models.Model):
    caption = models.CharField(max_length=50, db_index=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class ProductVisit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ip = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/products')

    def __str__(self):
        return self.product.title
