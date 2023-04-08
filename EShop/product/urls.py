from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('favorite-staff', views.Test.as_view(), name='Test'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail'),

]