from django.shortcuts import render, redirect

# Create your views here.
def submit_review(request):
    if request.method == 'POST':
        print("Review here")
    else:
        print("You are getting")
    return redirect('home')