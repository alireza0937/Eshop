from django.urls import path
from . import views

urlpatterns = [

    path('add_to_order', views.add_product_to_orders, name='add-to-order-page'),
    path('request/', views.send_request, name='request'),
    path('verify/', views.verify, name='verify'),


]
