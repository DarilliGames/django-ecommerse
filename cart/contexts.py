from django.shortcuts import get_object_or_404
from shop.models import SellItem


def cart_contents(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        product = get_object_or_404(SellItem, pk=id)
        total += quantity * product.price
        product_count += quantity
        product.ptotal = product.price * quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})

    return { 'cart_items': cart_items, 'total': total, 'product_count': product_count }