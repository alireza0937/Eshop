import datetime

from django.db import models
from account.models import User


class ArticleCategoryModels(models.Model):
    parent = models.ForeignKey('ArticleCategoryModels', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    url_title = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, db_index=True, allow_unicode=True)
    image = models.ImageField(upload_to='images/article')
    short_description = models.TextField()
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    selected_categories = models.ManyToManyField('ArticleCategoryModels')
    auther = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title


class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    parent = models.ForeignKey('Comments', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True,)
    message = models.TextField()
    is_span = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)
