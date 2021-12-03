from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from snappy.decorators import unauthenticated_user, allowerd_users

# Create your views here.
def index(request):
   
    context ={}
    return render(request, 'driver/home.html', context)


def registration(request):
       
    context ={}
    return render(request, 'driver/registration.html', context)


# @unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            messages.success(request, 'Welcome ' + username +'!')
            return redirect('index') 
            
    context ={}
    return render(request, 'driver/login.html', context)



def logoutPage(request):
    logout(request)
    return redirect('login')