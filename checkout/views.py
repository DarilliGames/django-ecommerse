from django.shortcuts import render, redirect
from .forms import MakePaymentForm, OrderForm
# Create your views here.
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
        form.save()
        return redirect("cart")
    else:
        return redirect("home")