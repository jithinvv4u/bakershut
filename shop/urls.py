from accounts.views import loadHome
from django.urls import path
from .views import *

urlpatterns = [
    path('home/',loadHome,name='shop_home'),
    path('orderproducts/',orderProducts,name='shop_orderproduct'),
    path('order/<id>',order,name='shop_order'),
    path('orderstatus/',orderStatus,name='shop_orderstatus'),
    path('addtocart/<id>',addCart,name='shop_cart'),
    path('removefromcart/<id>',removeCart,name='shop_removecart'),
    path('cart/',showCart,name='shop_showcart'),
    path('updateprofile/',updateProfile,name='shop_updateprofile'),
    path('changepassword/',changePassword,name='shop_changepassword'),
]