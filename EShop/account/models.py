from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profiles', blank=True, null=True)
    email_active_code = models.CharField(max_length=200, )
    about_user = models.TextField(null=True, blank=True)
    address = models.TextField(null=True)

    def __str__(self):
        return self.get_full_name()
