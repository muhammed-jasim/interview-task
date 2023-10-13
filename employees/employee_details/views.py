from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def Index (request):
    return render (request,'index.html')

def Terms (request):
    return render (request,'terms.html')

def Navbar(request):
    return render (request,'nav.html')

def signup(request):
    if request.method=="POST":      
        username=request.POST['username'] 
        email=request.POST['email']             
        password=request.POST['password']         
        cnfpassword=request.POST['cnfmpassword'] 
        if User.objects.filter(username=username).exists():
            messages.info(request,"username already exists")  
            return redirect('signup')                         
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email already taken")
            return redirect('signup')
        elif password != cnfpassword :                     
            messages.info(request,"password mismatch")      
            return redirect('signup')                     
        else:
            user=User.objects.create_user(username=username,email=email,password=password)                                                                              
            user.save();                 
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')                 
    else:
        return render(request,'signup.html') 


def Loginn(request):
    if request.method == "POST":   
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(username=username,password=password) 
        if user is not None :  
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,"invalid login")
    return render(request,'login.html')

 
def logout(request):
    auth.logout(request)  
    return render(request,'login.html')

def addemployee(request):
    if request.method == 'POST':
        name = request.POST['name']
        emp_id = request.POST['emp_id']
        email = request.POST['email']
        phone = request.POST['phone']
        employee = Employee()
        employee.emp_id = emp_id
        employee.name = name
        employee.email = email
        employee.phone = phone
        employee.save()
        return redirect('employeelist')
    else:
        return render (request,'addemployee.html')
    

def employee_list(request):
    employees = {
        'employees':Employee.objects.all
    }
    return render(request,'employeelist.html',employees)


def employee_dlt(request,i):
    emp = Employee.objects.get(id=i)
    emp.delete()
    return redirect('employeelist')

def update(request,i):
    global emp_update
    emp_update = Employee.objects.get(id=i)
    return render(request,'update.html',{'empupdate':emp_update})

def emp_doupdate (request):
        name = request.POST['name']
        emp_id = request.POST['emp_id']
        email = request.POST['email']
        phone = request.POST['phone']
        emp_update.emp_id = emp_id
        emp_update.name = name
        emp_update.email = email
        emp_update.phone = phone
        emp_update.save()
        return redirect('employeelist')
