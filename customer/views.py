from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from snappy.decorators import unauthenticated_user, allowerd_users
from .forms import OrderForm
from .models import Order
from datetime import datetime
from datetime import date
#import datetime
from django.utils import timezone
from django.db import IntegrityError
import json
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
import requests

now = datetime.now()
date1 = datetime.now().strftime('%M:%S.%f')
today = date.today()
year1 = today.strftime("%Y")
year2 = now.strftime("%m%d%Y%H%M%f")
# Create your views here.
def index(request):
   
    context ={}
    return render(request, 'customer/home.html', context)


def registration(request):
       
    context ={}
    return render(request, 'customer/registration.html', context)


val=None
def dispatch(request):
    initiator = request.user
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        stan = request.POST.get('stan')
        orderid = now.strftime("%m%d%Y%H%M%f")
        orderid=int(orderid)
        global val
        def val():
            return orderid
        try:
            if form.is_valid():
                order = form.save()
                order.orderid=orderid
                order.save()
                return redirect('payment')
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args): 
                entry= Order.objects.get(orderid= '')
                entry.delete()
                return redirect('payment')
    context ={"form":form}
    return render(request, 'customer/dispatch.html', context)


def payment(request):
    stan = val()
    key1 = settings.RAVE_PUBLIC_KEY
    stanid = Order.objects.get(orderid = stan)
    form = OrderForm(instance=stanid)
    initiator = request.user
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=stanid)
        try:
            if form.is_valid():
                form.save()
                return redirect('confirm')
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args): 
                messages.success(request, 'Welcome ' + username +'!')
                return redirect('index')
    context ={"form":form, "key1":key1, "stan":stan}
    return render(request, 'customer/payment.html', context)




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
    return render(request, 'customer/login.html', context)



def logoutPage(request):
    logout(request)
    return redirect('login')




@require_POST
@csrf_exempt
def my_webhook_view(request):
    request_json = json.loads(request.body)
    transaction_id = request_json.get('id')
    transaction_id = str(transaction_id)
    url = "https://api.flutterwave.com/v3/transactions/" + transaction_id + "/verify/"
    #payload="{\r\n\"id\":\"1935022\"\r\n}"
    headers = {'Content-Type': 'application/json','Authorization': 'Bearer FLWSECK_TEST-5f94dab00ea137b70706b1444aee4827-X'}
    response = requests.request("GET", url, headers=headers)
    request_json2 = json.loads(response.text)
    status = request_json2.get('status')
    if status == 'success':
        print(status)
        print(status)
        return redirect('confirm')
        #return HttpResponse(status=200)
    else:
        return redirect('confirm')
    context = {'response':response, "status":status}
    return render(request, 'pay.html', context)

    
def confirm(request):

    context ={}
    return render(request, 'customer/pay.html', context)








