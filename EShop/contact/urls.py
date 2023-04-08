from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUsView.as_view(), name='contact'),
    path('profile/', views.ProfileImage.as_view(), name='profile-image'),
    path('images/', views.ProfileImagesList.as_view(), name='profile-image-list'),

]
