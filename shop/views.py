from django.shortcuts import render,redirect,HttpResponse
from shop.models import Cart, OrderItems
from accounts.forms import *
from owner.models import Products
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# ----------------- Home -------------------------

@login_required()
def loadHome(request):
    return render(request,'shophome.html')

# ----------------- Products Page -----------------

@login_required()
def orderProducts(request):
    prod = Products.objects.all()
    context = {'product':prod}
    if request.method == 'GET':
        return render(request,'orderproduct.html',context)

# ------------------ Ordering Products ---------------

@login_required()
def order(request,id):
    prod = Products.objects.get(pk=id)
    context = {'product':prod}
    if request.method == 'GET':
        return render(request,'order.html',context)
    elif request.method == 'POST':
        qty = request.POST['qty']
        ord = OrderItems()
        ord.userid = request.user
        ord.productid = prod
        ord.qty = qty
        price = (float(qty)*prod.cost)-ord.discount
        ord.cost = price
        ord.ordertype = 'shop'
        ord.save()
        prod.stock -= int(ord.qty)
        prod.save()
        return HttpResponse('order placed')
    else:
        return HttpResponse('hi')

# --------------------- Order Status -------------------

@login_required()
def orderStatus(request):
    obj = OrderItems.objects.all()
    # print(obj)
    context = {'order':obj,'user':request.user}
    return render(request,'orderstatus.html',context)

# ---------------------- Adding products to cart ----------------------

@login_required()
def addCart(request,id):
    pro = Products.objects.get(pk=id)
    obj = Cart()
    obj.productid = pro
    obj.userid = request.user
    obj.save()
    return HttpResponse('item added to cart')

# ----------------------- Showing products in cart --------------------------

@login_required()
def showCart(request):
    obj = Cart.objects.all()
    # print(obj)
    context = {'order':obj}
    return render(request,'cart.html',context)

# ------------------------ Removing products from cart --------------------------

@login_required()
def removeCart(request,id):
    obj = Cart.objects.get(pk=id)
    obj.delete()
    return HttpResponse('item removed from cart')

# ------------------------ Update shop Profile --------------------------------

@login_required()
def updateProfile(request):
    context = {}
    context['form'] = UpdateForm(instance=request.user)
    if request.method == 'GET':
        return render(request,'shopupdateprofile.html',context)
    elif request.method == 'POST':
        form = UpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"profile updated successfully")
            return redirect('shop_updateprofile')
        else:
            messages.error(request,"error while submitting")
            return render(request,'shopupdateprofile.html',context)
    else:
        return redirect('owner_home')

# ------------------------ Change user password -----------------------------------

@login_required()        
def changePassword(request):
    if request.method == 'GET':
        return render(request,'shopchangepassword.html')
    if request.method == 'POST':
        new = request.POST['new']
        renew = request.POST['renew']
        if new==renew:
            request.user.set_password(new)
            request.user.save()
        else:
            messages.error(request,'passwords not matching,please re enter')
            return render(request,'shopchangepassword.html')
        return redirect('login')
