from django.urls import path
from . import views 


urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('registration/', views.registration, name='registration'),

]