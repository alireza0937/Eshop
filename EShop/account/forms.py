from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
    )
    password = forms.CharField(label='رمز عبور')
    password_repeat = forms.CharField(label='تکرار رمز عبور')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('password_repeat')
        if password == confirm_password:
            return confirm_password
        raise ValidationError("پسورد یکی نیست.")


class LoginForm(forms.Form):
    email = forms.EmailField(label='ایمیل', error_messages={'invalid': 'ایمیل وارد شده صحیح نیست'})
    password = forms.CharField(label='رمز عبور', error_messages={'invalid': 'رمز وارد شده صحیح نیست'})


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(label='ایمیل',error_messages={'invalid': 'ایمیل وارد شده یافت نشد'})


class ResetPasswordForm(forms.Form):
    password = forms.CharField(label='رمز عبور')
    password_repeat = forms.CharField(label='تکرار رمز عبور')
