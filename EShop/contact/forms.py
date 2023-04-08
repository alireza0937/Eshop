from django import forms
from .models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["title",
                  'full_name',
                  'email',
                  'message',
                  ]

        widgets = {
            "full_name": forms.TextInput(attrs={
                'placeholder': 'نام و نام خانوادگی',
                'class': 'form-control',
            }),

            "email": forms.TextInput(attrs={
                'placeholder': 'example@gmail.com',
                'class': 'form-control',
            }),

            "title": forms.TextInput(attrs={
                'placeholder': 'موضوع',
                'class': 'form-control',
            }),

            "message": forms.Textarea(attrs={
                'placeholder': 'متن پیام',
                'class': 'form-control',
                'row': 5,
                'id': 'message'
            }),
        }

        labels = {
            'full_name': "نام و نام خانوادگی",
            'email': 'ایمیل',
            'title': 'موضوع',
            'message': 'پیام'
        }


class ProfileImagesForm(forms.Form):
    user_image = forms.ImageField()

