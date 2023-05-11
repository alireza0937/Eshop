from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.HomeView.as_view(), name='index-page'),
    path('about/', views.AboutUsView.as_view(), name='AboutUs-page'),
   
]