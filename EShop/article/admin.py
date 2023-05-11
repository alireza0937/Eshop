from django.contrib import admin
from . import models
from .models import ArticleCategoryModels


class ArticleCategoriesAdmin(admin.ModelAdmin):
    pass
    list_display = ['title', 'parent']


admin.site.register(models.ArticleCategoryModels, ArticleCategoriesAdmin)
admin.site.register(models.Article)
admin.site.register(models.Comments)
