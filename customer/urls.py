from django.urls import path
from .views import *

urlpatterns = [
    path('home/',loadHome,name='customer_home'),
    path('orderproducts/',custOrderProducts,name='customer_orderproduct'),
    path('order/<id>',custOrder,name='customer_order'),
    path('orderstatus/',custOrderStatus,name='customer_orderstatus'),
    path('addtocart/<id>',custAddCart,name='customer_cart'),
    path('removefromcart/<id>',custRemoveCart,name='customer_removecart'),
    path('cart/',custShowCart,name='customer_showcart'),
    path('updateprofile/',custUpdateProfile,name='customer_updateprofile'),
    path('changepassword/',custChangePassword,name='customer_changepassword'),
]