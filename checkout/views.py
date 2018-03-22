from django.shortcuts import render, redirect, get_object_or_404
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from shop.models import SellItem
from cart.contexts import cart_contents
import stripe



def checkout(request):
    order_form = OrderForm()
    payment_form = MakePaymentForm()
    return render(request, "checkout/checkout.html", {"order_form":order_form, "payment_form":payment_form})
    
    
def process(request):
    if request.method =="POST":
        form = OrderForm(request.POST)
        pform = MakePaymentForm(request.POST)
        if request.user.is_authenticated:
            print(request.user)
        order = form.save()
        cart = request.session["cart"]
        total = 0
        for id, quantity in cart.items():
            oli = OrderLineItem()
            product = get_object_or_404(SellItem, pk=id)
            total += product.price * quantity
            oli.product = product
            oli.order = order
            oli.quantity = quantity
            oli.save()
        print(total)
        
        del request.session["cart"]
        
        return redirect("cart")
    else:
        return redirect("home")