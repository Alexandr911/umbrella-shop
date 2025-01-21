from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order
from cart.models import CartItem

def create_order(request):
    session_key = request.session.session_key
    if not session_key:
        return redirect('cart_detail')  # Если корзина пуста, перенаправляем на страницу корзины

    cart_items = CartItem.objects.filter(session_key=session_key)
    if not cart_items:
        return redirect('cart_detail')  # Если в корзине ничего нет, перенаправляем пользователя

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()  # Сохраняем заказ

            # Удаляем товары из корзины
            cart_items.delete()

            return render(request, 'orders/order_success.html', {'order': order})

    else:
        form = OrderForm()

    return render(request, 'orders/order_form.html', {'form': form})