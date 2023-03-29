from django.db import models

# Create your models here.

class ContactUs(models.Model):
    title = models.CharField(max_length=70)
    email = models.EmailField(max_length=200)
    full_name = models.CharField(max_length=300)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    response = models.TextField(null=True, blank=True)
    is_read_by_admin = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title
    


