from django.shortcuts import render, redirect
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import Order, OrderItem


def create_order_items(order, cart):
    for item in cart:
        OrderItem.objects.create(
            order=order,
            product=item['product'],
            price=item['price'],
            quantity=item['quantity']
        )


def order_create(request):
    cart = Cart(request)

    if request.user.is_authenticated:
        profile = getattr(request.user, 'profile', None)

        if profile and request.user.first_name and request.user.last_name and request.user.email:
            order = Order.objects.create(
                user=request.user,
                first_name=request.user.first_name,
                last_name=request.user.last_name,
                email=request.user.email,
                phone_number=profile.phone_number,
                address=profile.address,
                city=profile.city,
            )

            create_order_items(order, cart)
            cart.clear()
            return render(request, 'order/order_create.html', {'order': order})

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.save()

            create_order_items(order, cart)
            cart.clear()
            return render(request, 'order/order_create.html', {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, 'order/order_create.html', {'form': form, 'cart': cart})
