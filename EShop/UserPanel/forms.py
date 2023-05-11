from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpRequest

from account.models import User


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'about_user',
            'address',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'نام',
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'نام خانوادگی',
                'class': 'form-control'
            }),
            'about_user': forms.Textarea(attrs={
                'placeholder': 'درباره من',
                'class': 'form-control',
                'row': 2,
                'id': 'message',
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'ادرس',
                'class': 'form-control',

            })
        }

        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'about_user': 'درباره من',
            'address': 'ادرس',
        }


class ChangePasswordModel(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'password'
        ]

        widgets = {
            'password': forms.PasswordInput(attrs={
                'class': 'form-control'
            })
        }

        labels = {
            'password': 'رمز عبور',
        }


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='کلمه عبور فعلی',
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))
    new_password = forms.CharField(
        label='کلمه عبور جدید',
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))
    repeat_password = forms.CharField(
        label=' تکرار کلمه عبور ',
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))

    def clean_confirm_password(self):
        new_password = self.cleaned_data.get('new_password')
        repeat_password = self.cleaned_data.get('repeat_password')
        if new_password == repeat_password:
            return new_password

        raise ValidationError("کلمه عبور و تکرار ان مغایرت دارند")




