from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('cat/<cat>/', views.ProductListView.as_view(), name='product_cat'),
    path('brand/<brand>/', views.ProductListView.as_view(), name='product_brand'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail'),


]