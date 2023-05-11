from django.db import models


# Create your models here.
class SiteSettings(models.Model):
    site_name = models.CharField(max_length=50)
    site_url = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    fax = models.CharField(max_length=50)
    email = models.EmailField()
    copy_right = models.CharField(max_length=200)
    about_us_text = models.CharField(max_length=200)
    site_logo = models.ImageField(upload_to='images/site-setting')
    is_main_setting = models.BooleanField()

    def __str__(self):
        return self.site_name


class SliderSetting(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=500)
    url_title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='images/slider')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class AdvModel(models.Model):
    class BannerPosition(models.TextChoices):
        product_list = 'product_list', 'لیست محصولات'
        product_detail = 'product_detail', 'جزئیات محصولات'
        about_us = 'about_us', 'درباره ما'

    banner = models.ImageField(upload_to='images/advertise')
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField()
    position = models.CharField(max_length=200, choices=BannerPosition.choices)

    def __str__(self):
        return self.title




