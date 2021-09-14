from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.

# -------------------- Main Page -----------------------

def loadHome(request):
    return render(request,'index.html')

# -------------------- Login Page ----------------------

def userLogin(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname,password=pwd)
        if user != None:
            type = user.usertype
            login(request,user)
            request.session['username']=uname
            if type == 'admin':
                return redirect('/admin/')
            elif type == 'owner':
                return redirect('owner_home')
            elif type == 'staff':
                return redirect('staff_home')
            elif type == 'shop':
                return redirect('shop_home')
            elif type == 'customer':
                return redirect('customer_home')
            else:
                return HttpResponse('requested page unavailable')
        else:
            context = {}
            context['msg'] = 'Invalid username and password'
            return render(request,'login.html',context)

# ----------------------- Registering user as Shop ---------------------------

def RegisterShop(request):
    context = {'form1':UserForm(initial={'usertype':'shop'}),'form2':ShopForm()}
    if request.method == 'GET':
        return render(request,'shopregistration.html',context)
    elif request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = ShopForm(request.POST)
        pwd = request.POST['password']
        if form1.is_valid() and form2.is_valid():
            obj1 = form1.save(commit=False)
            obj2 = form2.save(commit=False)
            obj2.login = obj1
            obj1.set_password(pwd)
            obj1.save()
            obj2.save()
            return HttpResponse('user registered as shop')
        else:
            return render(request,'shopregistration.html',{'form1':form1,'form2':form2})
    else:
        return render(request,'shopregistration.html',context)

# ---------------------- Registering user as customer ----------------------------

def RegisterCust(request):
    context = {'form1':UserForm(initial={'usertype':'customer'})}
    if request.method == 'GET':
        return render(request,'customerregistration.html',context)
    elif request.method == 'POST':
        form1 = UserForm(request.POST)
        pwd = request.POST['password']
        if form1.is_valid():
            obj1 = form1.save(commit=False)
            obj1.set_password(pwd)
            obj1.save()
            return HttpResponse('user registered as customer')
        else:
            return render(request,'customerregistration.html',{'form1':form1})
    else:
        return render(request,'customerregistration.html',context)

# ------------------------- Logout user -----------------------------------------

def userLogout(request):
    logout(request)
    return redirect('login')