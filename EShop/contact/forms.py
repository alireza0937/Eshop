from django import forms
from .models import ContactUs


class ContactUsForm(forms.Form):
    full_name = forms.CharField(
        label='نام و نام خانوادگی', 
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'نام و نام خانوادگی'
        })
    )

    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'placeholder': 'example@email.com'
        })
    )

    title = forms.CharField(
        label='موضوع',
        widget=forms.TextInput(attrs={
            'placeholder': 'موضوع'
            })
    )
    
    message = forms.CharField(
        label='پیام',
        widget=forms.Textarea(attrs={
            'placeholder': 'متن پیام'  
            }) 
    )


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
            'placeholder':'نام و نام خانوادگی',
            'class': 'form-control',
            }),

            "email": forms.TextInput(attrs={
            'placeholder':'example@gmail.com',
            'class': 'form-control',
            }),

            "title": forms.TextInput(attrs={
            'placeholder':'موضوع',
            'class': 'form-control',
            }),
            
            "message": forms.Textarea(attrs={
            'placeholder': 'متن پیام',
            'class': 'form-control',
            'row': 5,
            'id':'message'
            }),
        }
        
        labels = {
            'full_name':"نام و نام خانوادگی",
            'email': 'ایمیل',
            'title': 'موضوع',
            'message': 'پیام'
        }
  