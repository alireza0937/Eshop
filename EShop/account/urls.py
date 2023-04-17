from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register-page'),
    path('login/', views.LoginView.as_view(), name='login-page'),
    path('logout/', views.LogoutView.as_view(), name='logout-page'),
    path("activate/<email_activation_code>/", views.verificationcode1, name='activation-account'),
    path('forget-password/', views.ForgetPassword.as_view(), name='forget-password-page'),
    path("reset_password/<active_code>/", views.ResetPassword.as_view(), name='reset-password-page'),


]