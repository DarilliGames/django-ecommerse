from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
 


                                    #                   Log out redirects to the same page you were on                  #



def logout(request):
    auth.logout(request)
    url = request.META.get('HTTP_REFERER')
    messages.success(request, "you logged out successfully")
    return HttpResponseRedirect(url)

def login(request):
    for k in request.GET:
        print(request.GET[k])
    redirect_to = request.GET.get('next', 'home')
    if request.method=='POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            #Authenticate the user
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password'))
            # if the user is a user, and has correct password
            if user is not None:
                #Log them in
                auth.login(request, user)
                messages.success(request, "You have sucessfully logged out")
                return redirect(redirect_to)
            else:
                # say no
                form.add_error(None, "Your username or password was not recognised")
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', { 'form': form })

@login_required()
def yourprofile(request):
    return render(request, 'accounts/yourprofile.html')
    
def profile(request, id):
    person = get_object_or_404(User, pk=id)
    return render(request, 'accounts/profile.html', {"person":person})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))
            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect('yourprofile')
            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})



@login_required()
def remove_profile(request, id):
    profile = get_object_or_404(User, pk=id)
    if request.user.id == profile.id or request.user.is_staff:
        auth.logout(request)
        profile.delete()
    return redirect('home')
