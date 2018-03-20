from django.shortcuts import render, redirect, get_object_or_404
from .forms import SellItemForm
from .models import SellItem
# Create your views here.


def upload_sale(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = SellItemForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.seller = request.user
                
                post.save()
            return redirect("home")
        else:
            form = SellItemForm()
            return render(request, "shop/uploadsale.html", {'form':form})
    else:
        return redirect('home')
        
def display_self(request):
    prods = SellItem.objects.all()
    return render(request, "shop/displayshelf.html", {'prods':prods})
    
        
def display_product(request, id):
    item = get_object_or_404(SellItem, pk=id)
    return render(request, "shop/product.html", {"item" : item})