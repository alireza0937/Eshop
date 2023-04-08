from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class ProductBrand(models.Model):
    title = models.CharField(max_length=300, db_index=True)
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
    price = models.IntegerField()
    brand = models.ForeignKey(ProductBrand, null=True, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=500, null=True, db_index=True)
    description = models.TextField(db_index=True)
    slug = models.SlugField(default="", null=False, db_index=True, editable=False, max_length=200, unique=True)
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField()

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


