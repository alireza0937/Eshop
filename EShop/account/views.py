from django.http import HttpResponse, Http404, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from .forms import RegisterForm, LoginForm, ForgetPasswordForm, ResetPasswordForm
from .models import User
from django.contrib.auth import login, logout


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        data = {
            'registration_form': form,
        }
        return render(request, 'account/register.html', context=data)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=email).exists()
            if user:
                form.add_error('ایمیل تکراری است')
            else:
                new_user = User(
                    email=email,
                    email_active_code=get_random_string(15),
                    is_active=False,
                    username=email, )
                new_user.set_password(password)
                new_user.save()
                return redirect(reverse('index-page'))

        form = RegisterForm()
        data = {
            'registration_form': form,
        }
        return render(request, 'account/register.html', context=data)


def verificationcode1(request, email_activation_code):
    user = User.objects.filter(email_active_code__iexact=email_activation_code).first()
    print(user)
    if user is not None:
        user.is_active = True
        user.save()
        return redirect(reverse('register-page'))
    else:
        raise Http404


class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        data = {
            "login_form": login_form,
        }
        return render(request, 'account/login.html', context=data)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            print(user_email)
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری فعال نشده است.')
                else:
                    is_password_correct = user.check_password(user_password)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('index-page'))

                    else:
                        login_form.add_error('password', 'رمز وارد شده اشتباه است')

            else:
                login_form.add_error('email', 'حساب کاربری یافت نشد')

        data = {
            "login_form": login_form,
        }
        return render(request, 'account/login.html', context=data)


class ForgetPassword(View):

    def get(self, request: HttpRequest):
        user_form = ForgetPasswordForm()
        data = {
            'form': user_form,
        }
        return render(request, 'account/forget-password.html', context=data)

    def post(self, request: HttpRequest):
        user_form = ForgetPasswordForm(request.POST)

        if user_form.is_valid():
            user_email = user_form.cleaned_data.get('email')
            user_exist = User.objects.filter(email__iexact=user_email).first()
            if user_exist is not None:
                return render(request, 'account/sent-mail.html')
            else:
                return render(request, 'account/forget-password.html', context={'wrong_email': True})


class ResetPassword(View):
    def get(self, request, active_code):
        user = User.objects.filter(email_active_code__exact=active_code).first()
        if user is None:
            return redirect(reverse('index-page'))
        else:
            form = ResetPasswordForm()
            return render(request, 'account/reset-password.html', context={'form': form,
                                                                           'user': user})

    def post(self, request: HttpRequest, active_code):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            user: User = User.objects.filter(email_active_code__iexact=active_code).first()
            user_new_password = form.cleaned_data.get('password_repeat')
            user.set_password(user_new_password)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('login-page'))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('index-page'))

