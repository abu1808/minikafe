from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.base_view, name='base'),
    path('menu/', views.menu_view, name='menu'),
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart_view, name='add_to_cart'),
    path('orders/', views.orders_view, name='orders'),
    path('add_menu_item/', views.add_menu_item, name='add_menu_item'),
    path('register/', views.register_view, name='register'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('delivery/', views.delivery_view, name='delivery'),
    path('admin_menu/', views.admin_menu_view, name='admin_menu'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] 
