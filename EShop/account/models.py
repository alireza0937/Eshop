from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render


class User(AbstractUser):
    avatar = models.CharField(max_length=20, null=True, blank=True)
    email_active_code = models.CharField(max_length=200,)

    def __str__(self):
        return self.get_full_name()