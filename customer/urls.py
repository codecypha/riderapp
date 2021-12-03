from django.urls import path
from . import views 


urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('dispatch/', views.dispatch, name='dispatch'),
    path('payment/', views.payment, name='payment'),
    path('verify/', views.my_webhook_view, name='verify'),
    path('confirmation/', views.confirm, name='confirm'),
]