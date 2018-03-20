from django.shortcuts import render

# Create your views here.

def upload_sale(request):
    return render(request, "shop/upload.html")