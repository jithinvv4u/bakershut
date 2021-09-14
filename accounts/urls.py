from django.urls import path
from .views import *

urlpatterns = [
    path('login/',userLogin,name='login'),
    path('shopregistration/',RegisterShop,name='shop_register'),
    path('customerregistration/',RegisterCust,name='customer_register'),
    path('logout/',userLogout,name='logout')
]
