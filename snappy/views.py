from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowerd_users
from .forms import DriverForm
from .models import Driver
from datetime import datetime
from datetime import date
import datetime
from django.utils import timezone
from django.conf import settings

today = date.today()
year1 = today.strftime("%Y")

# Create your views here.
@login_required(login_url  ='login')
def index(request):   
    initiator = request.user
    all_drivers = Driver.objects.all()
    context ={'initiator':initiator, "all_drivers":all_drivers, "year1":year1}
    return render(request, 'snappy/dashboard.html', context)


def add_driver(request):   
    initiator = request.user
    form = DriverForm(request.FILES)
    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context ={"form":form}
    return render(request, 'snappy/add_driver.html', context)


def all_driver(request):   
    initiator = request.user
    all_drivers = Driver.objects.all()

    
    context ={'all_drivers':all_drivers}
    return render(request, 'snappy/all_drivers.html', context)


def edit_driver(request):   
    initiator = request.user
    
    context ={}
    return render(request, 'snappy/edit_driver.html', context)


def delete_driver(request):   
    initiator = request.user
    
    context ={}
    return render(request, 'snappy/delete_driver.html', context)


def driver_payment(request):   
    initiator = request.user
    
    context ={}
    return render(request, 'snappy/driver_payment.html', context)


@unauthenticated_user
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
    return render(request, 'snappy/login.html', context)



def logoutPage(request):
    logout(request)
    return redirect('login')


