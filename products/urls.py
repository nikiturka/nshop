from django.urls import path
from . import views


urlpatterns = [
    path('id=<product_id>', views.product_view, name='product'),
    path('cart_add', views.cart_add, name='cart_add')
]
