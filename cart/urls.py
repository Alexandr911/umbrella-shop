from django.urls import path
from .views import add_to_cart
from .views import cart_detail
from .views import remove_from_cart
from . import views

urlpatterns = [
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('', cart_detail, name='cart_detail'),
    path('', views.cart_detail, name='cart_detail'),  # Корзина

]