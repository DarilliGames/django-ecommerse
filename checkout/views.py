from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from shop.models import SellItem
from cart.contexts import cart_contents
from django.conf import settings
import stripe


stripe.api_key = settings.STRIPE_SECRET

def checkout(request):
    order_form = OrderForm()
    payment_form = MakePaymentForm()
    return render(request, "checkout/checkout.html", {"order_form":order_form, "payment_form":payment_form, "publishable": settings.STRIPE_PUBLISH})
    
    
def process(request):
    if request.method =="POST":
        form = OrderForm(request.POST)
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
            print("Order In")
            
        pform = MakePaymentForm(request.POST)
        if pform.is_valid():
            if request.user.is_authenticated:
                mail = request.user.mail
            else:
                mail = (form.cleaned_data["full_name"])
            try:
                customer = stripe.Charge.create(
                    amount= int(total * 100),
                    currency="EUR",
                    description=mail,
                    card=pform.cleaned_data['stripe_id'],
                    )
                    
                if customer.paid:
                    messages.success(request, "You have sucessfully logged out")
                    print("Paid")
                        
                        
                    request.session['cart'] = {}
                    return redirect('home')
                    
            except stripe.error.CardError:
                messages.error(request, "Card Invalid")
                print("Invalid")
    
                
        else:
            messages.error(request, "No")
            print("Card Not Valid")
        
        payment_form = MakePaymentForm(request.POST)
        order_form = OrderForm(request.POST)
        
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout/checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISH })