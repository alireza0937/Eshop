from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_dashboard, name='user-dashboard'),
    path('user/shopping/', views.ShopHistory.as_view(), name='user-shopping-page'),
    path('user/shopping/<pk>', views.show_order_details, name='order-detail-page'),
    path('user/edit/', views.EditProfile.as_view(), name='edit-profile'),
    path('user/cart/', views.user_basket, name='user-cart-page'),
    path('user/cart/amount', views.change_amount_of_product, name='change-amount-page'),
    path('user/cart/remove', views.remove_product, name='remove-product-page'),
    path('user/edit/changepass/', views.ChangePassword.as_view(), name='change-password'),
]
