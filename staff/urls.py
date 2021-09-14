from django.urls import path
from .views import *

urlpatterns = [
   path('home/',staffHome,name='staff_home'),
   path('shops/',shopList,name='staff_shoplist'),
   path('customers/',custList,name='staff_custlist'),
   path('managecustomerorder/',manageCustOrder,name='staff_managecustorder'),
   path('manageshoporder/',manageShopOrder,name='staff_manageshoporder'),
   path('deliverorder/<id>',deliverShop,name='staff_delivershop'),
   path('deliverorder/<id>',deliverCust,name='staff_delivercust'),
   path('changepassword/',changePassword,name='staff_changepassword'),
   path('updateprofile/',updateProfile,name='staff_updateprofile'),
]
