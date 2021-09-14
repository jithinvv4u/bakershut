from django.shortcuts import render,redirect,HttpResponse
from owner.models import *
from accounts.forms import *
from shop.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# ----------------- Home -------------------------

@login_required()
def loadHome(request):
    return render(request,'custhome.html')

# ----------------- Products Page -----------------

@login_required()
def custOrderProducts(request):
    prod = Products.objects.all()
    context = {'product':prod}
    if request.method == 'GET':
        return render(request,'orderproduct.html',context)

# ------------------ Ordering Products ---------------

@login_required()
def custOrder(request,id):
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
        ord.ordertype = 'customer'
        ord.save()
        prod.stock -= int(ord.qty)
        prod.save()
        return HttpResponse('order placed')
    else:
        return HttpResponse('hi')

# --------------------- Order Status -------------------

@login_required()
def custOrderStatus(request):
    obj = OrderItems.objects.all()
    print(obj)
    context = {'order':obj,'user':request.user}
    return render(request,'orderstatus.html',context)

# ---------------------- Adding products to cart ----------------------

@login_required()
def custAddCart(request,id):
    pro = Products.objects.get(pk=id)
    obj = Cart()
    obj.productid = pro
    obj.userid = request.user
    obj.save()
    return HttpResponse('item added to cart')

# ----------------------- Showing products in cart --------------------------

@login_required()
def custShowCart(request):
    obj = Cart.objects.all()
    # print(obj)
    context = {'order':obj}
    return render(request,'cart1.html',context)

# ------------------------ Removing products from cart --------------------------

@login_required()
def custRemoveCart(request,id):
    obj = Cart.objects.get(pk=id)
    obj.delete()
    return HttpResponse('item removed from cart')

# ------------------------ Update customer Profile --------------------------------

@login_required()
def custUpdateProfile(request):
    context = {}
    context['form'] = UpdateForm(instance=request.user)
    if request.method == 'GET':
        return render(request,'custupdateprofile.html',context)
    elif request.method == 'POST':
        form = UpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"profile updated successfully")
            return redirect('customer_updateprofile')
        else:
            messages.error(request,"error while submitting")
            return render(request,'custupdateprofile.html',context)
    else:
        return redirect('customer_home')

# ------------------------ Change user password -----------------------------------

@login_required()
def custChangePassword(request):
    if request.method == 'GET':
        return render(request,'custchangepassword.html')
    if request.method == 'POST':
        new = request.POST['new']
        renew = request.POST['renew']
        if new==renew:
            request.user.set_password(new)
            request.user.save()
        else:
            messages.error(request,'passwords not matching,please re enter')
            return render(request,'custchangepassword.html')
        return redirect('login')