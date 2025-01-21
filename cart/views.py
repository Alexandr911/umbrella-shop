from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from .models import CartItem
from products.models import Product

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    cart_item, created = CartItem.objects.get_or_create(
        product=product,
        session_key=session_key
    )
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return JsonResponse({"message": "Product added to cart", "quantity": cart_item.quantity})


def cart_detail(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    cart_items = CartItem.objects.filter(session_key=session_key)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart/cart_detail.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })