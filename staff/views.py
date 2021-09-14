from django.shortcuts import render,redirect
from shop.models import OrderItems
from accounts.models import *
from accounts.forms import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

# ----------------------- Staff Home -----------------------

@login_required()
def staffHome(request):
    return render(request,'staffhome.html')

# ----------------------- Shop List ------------------------

@login_required()
def shopList(request):
    list = ShopDetails.objects.all()
    context = {'shop':list}
    return render(request,'shoplists.html',context)

# ----------------------- Customer List ------------------------

@login_required()
def custList(request):
    list = UserLogin.objects.all()
    context = {'cust':list}
    return render(request,'customerlists.html',context)

# ----------------------- Managing Customer Order -----------------

@login_required()
def manageCustOrder(request):
    list = OrderItems.objects.all()
    context = {'order':list}
    return render(request,'customerorders.html',context)

# ----------------------- Managing Shop Order ---------------------

@login_required()
def manageShopOrder(request):
    list = OrderItems.objects.all()
    context = {'order':list}
    return render(request,'shoporders.html',context)

# ----------------------- Deliver Shop Ordered Products ------------------------

@login_required()
def deliverShop(request,id):
    obj = OrderItems.objects.get(pk=id)
    obj.status = 1
    obj.save()
    return redirect('staff_manageshoporder')

# ----------------------- Deliver Customer Ordered Products ------------------------

@login_required()
def deliverCust(request,id):
    obj = OrderItems.objects.get(pk=id)
    obj.status = 1
    obj.save()
    return redirect('staff_managecustorder')

# ----------------------- Change Password -------------------------

@login_required()
def changePassword(request):
    if request.method == 'GET':
        return render(request,'staffchangepassword.html')
    elif request.method == 'POST':
        new = request.POST['new']
        renew = request.POST['renew']
        if new==renew:
            request.user.set_password(new)
            request.user.save()
        else:
            messages.error(request,'passwords not matching,please re enter')
            return render(request,'staffchangepassword.html')
        return redirect('login')

# ------------------------ Update Profile -----------------------------

@login_required()
def updateProfile(request):
    context = {}
    context['form'] = UpdateForm(instance=request.user)
    if request.method == 'GET':
        return render(request,'staffupdateprofile.html',context)
    elif request.method == 'POST':
        form = UpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"profile updated successfully")
            return redirect('staff_updateprofile')
        else:
            messages.error(request,"error while submitting")
            return render(request,'staffupdateprofile.html',context)
    else:
        return redirect('owner_home')