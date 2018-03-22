from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import SellItemForm
from .models import SellItem
from reviews.forms import ReviewForm
from reviews.models import Review

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
    reviewform = ReviewForm()
    reviews = Review.objects.filter(item = id)
    return render(request, "shop/product.html", {"item" : item, "reviews":reviews, "reviewform":reviewform})
    
def add_to_cart(request, id):
    return redirect('home')
    
def review_item(request, id):
    if request.method == "POST":
        score = int(request.POST.get("score"))
        item = get_object_or_404(SellItem, pk=id)
        item.rating += score
        item.reviews += 1
        item.save()
        form = ReviewForm(request.POST)
        if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.item = item
                post.rating = score
                post.save()
        return redirect(reverse('product', args=id))
    else:
        return redirect(reverse('product', args=id))