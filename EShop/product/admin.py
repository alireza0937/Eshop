from django.contrib import admin
from .models import *

# Register your models here.



admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductTags)
admin.site.register(ProductBrand)
admin.site.register(ProductGallery)