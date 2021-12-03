from django.urls import path
from . import views 


urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('add_driver/', views.add_driver, name='add_driver'),
    path('edit_driver/', views.edit_driver, name='edit_driver'),
    path('delete_driver/', views.delete_driver, name='delete_driver'),
    path('all_driver/', views.all_driver, name='all_driver'),
    path('driver_payment/', views.driver_payment, name='driver_payment'),
]