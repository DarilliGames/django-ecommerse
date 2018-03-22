from django.shortcuts import render, redirect

def cart(request):
    return render(request, "cart/cart.html")

def add_to_cart(request):
    quantity=int(request.POST.get('ammount'))
    id=request.POST['item']
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    request.session["cart"] = cart
    print(cart)
    return redirect('shelf')

def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    cart.pop(id)
    request.session["cart"] = cart
    return redirect('cart')

def add_count_cart(request, id):
    cart = request.session.get('cart', {})
    cart[id] += 1
    request.session["cart"] = cart
    return redirect('cart')

def dec_count_cart(request, id):
    cart = request.session.get('cart', {})
    cart[id] -= 1
    if cart[id] == 0:
        cart.pop(id)
    request.session["cart"] = cart
    return redirect('cart')
    
def updatecart(request, id):
    cart = request.session.get('cart', {})
    quantity = request.GET.get("quantity")
    cart[id] = int(quantity)
    request.session["cart"] = cart
    return redirect('cart')
    
def dumpcart(request):
    del request.session["cart"]
    return redirect('home')