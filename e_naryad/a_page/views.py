from django.db import connection
from django.shortcuts import render, redirect
from django.urls import path
from .models import *
from django.contrib.auth.models import Group
from .forms import OrderForm, EmployeeForm, CreateNar1Form, CreateNar2Form, CreateNar3Form, CreateNar4Form
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, unauthenticated_user, admin_only
from django.db import connection
from django.db.models import Q
from collections import namedtuple

# Create your views here.

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


@login_required(login_url='login')
def enar(request):
    
    return render(request, 'enar.html')



@login_required(login_url='login')
def create_nar_page1(request):
    form = CreateNar1Form()

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = CreateNar1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enar')


    context={'form':form}

    return render(request, 'create_nar_page1.html', context)

@login_required(login_url='login')
def create_nar_page2(request):

    form = CreateNar2Form()

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = CreateNar2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enar')


    context={'form':form}
    return render(request, 'create_nar_page2.html', context)


@login_required(login_url='login')
def create_nar_page3(request):
    form = CreateNar3Form()

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = CreateNar3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enar')

    context = {'form':form}
    return render(request, 'create_nar_page3.html', context)

@login_required(login_url='login')
def create_nar_page4(request):

    form = CreateNar4Form()

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = CreateNar4Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enar')


    context={'form':form}
    return render(request, 'create_nar_page4.html', context)

@login_required(login_url='login')
def mainpage(request):

    return render(request, 'mainpage.html')

@login_required(login_url='login')
def open_nar_page1(request):
    return render(request, 'open_nar_page1.html')



@login_required(login_url='login')
def close_nar_page1(request):
    return render(request, 'close_nar_page1.html')



@login_required(login_url='login')
def order_index(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM a_page_order")
    orders = dictfetchall(cursor)

    print(orders)
    print(connection.queries)
    # orders = Order.objects.all()
    # print(orders)

    

    context={'orders':orders}
    return render(request, 'order/order_index.html', context) 



@login_required(login_url='login')
def order_edit(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order) 

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_i')

    context={'form':form}
    return render(request, 'order/order_add.html', context)


@login_required(login_url='login')
def order_add(request):

    form = OrderForm()
    
    
    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_i')


    context={'form':form}
    return render(request, 'order/order_add.html', context)


@login_required(login_url='login')
def passport_i(request):
    return render(request, 'passport/passport_index.html')



@login_required(login_url='login')
def passport_cabel(request):
    return render(request, 'passport/passport_cabel.html')



@login_required(login_url='login')
def passport_circuit(request):
    return render(request, 'passport/passport_circuit.html')



@login_required(login_url='login')
def passport_distribution(request):
    return render(request, 'passport/passport_distribution.html')



@login_required(login_url='login')
def passport_blade(request):
    return render(request, 'passport/passport_blade.html')



@login_required(login_url='login')
def passport_indoor(request):
    return render(request, 'passport/passport_indoor.html')



@login_required(login_url='login')
def passport_isg(request):
    return render(request, 'passport/passport_isg.html')



@login_required(login_url='login')
def passport_list(request):
    return render(request, 'passport/passport_list.html')



@login_required(login_url='login')
def passport_mcc(request):
    return render(request, 'passport/passport_mcc.html')



@login_required(login_url='login')
def passport_motor(request):
    return render(request, 'passport/passport_motor.html')



@login_required(login_url='login')
def passport_panel(request):
    return render(request, 'passport/passport_panel.html')



@login_required(login_url='login')
def passport_pg(request):
    return render(request, 'passport/passport_panel.html')



@login_required(login_url='login')  
def passport_substation(request):
    return render(request, 'passport/passport_substation.html')


@login_required(login_url='login')
def passport_uts(request):
    return render(request, 'passport/passport_uts.html')


@login_required(login_url='login')
def contact(request):
    return render(request, 'attendance/contact.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['employees'])
def calendar(request):
    return render(request, 'attendance/calendar.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['employees'])
def gate(request):
    return render(request, 'attendance/gate.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['employees'])
def add_sick(request):
    return render(request, 'attendance/add_sick.html')

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
            
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('enar')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context ={}          
    return render(request, 'login.html',context)



def logOutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def employee_list(request):
    employee = Employee.objects.all()
    employee_time = Employee_Time.objects.all()
    context={'employee':employee, 'employee_time':employee_time}
    return render(request, 'employee_list.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def employee(request,pk_test):
    employee = Employee.objects.filter(id=pk_test)
    employee_time = Employee_Time.objects.filter(id=pk_test)
    context={'employee':employee, 'employee_time':employee_time}
    return render(request, 'employee.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['employees'])
def flexi_time(request):
    return render(request, 'attendance/flexi_time.html')



@login_required(login_url='login')
@allowed_users(allowed_roles=['employees'])
def add_holiday(request):
    return render(request, 'attendance/add_holiday.html')



@login_required(login_url='login')
@allowed_users(allowed_roles=['employees'])
def plan_index(request):
    return render(request, 'plan/plan_index.html')



@login_required(login_url='login')
@allowed_users(allowed_roles=['employees'])
def messages_index(request):
    return render(request, 'messages/mess_index.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['employees'])
def accountSettings(request):
    employee=request.user.employee
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES ,instance=employee)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request, 'accountSettings.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['employees'])
def timer(request):
    return render(request, 'attendance/timer.html')