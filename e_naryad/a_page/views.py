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

def dictfetchone(cursor):
    for one in cursor:
        return one

@login_required(login_url='login')
def enar(request):
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM a_page_сreate_e_naryad_table_1")
    number = dictfetchone(cursor)
    nu = number[0]

    cursor1 = connection.cursor()
    cursor1.execute("SELECT COUNT(*) FROM a_page_сreate_e_naryad_table_2")
    number1 = dictfetchone(cursor1)
    nu1 = number1[0]

    cursor2 = connection.cursor()
    cursor2.execute("SELECT COUNT(*) FROM a_page_create_e_naryad_table_3")
    number2 = dictfetchone(cursor2)
    nu2 = number2[0]

    cursor3 = connection.cursor()
    cursor3.execute("SELECT COUNT(*) FROM a_page_create_e_naryad_table_4")
    number3 = dictfetchone(cursor3)
    nu3 = number3[0]

    nu4 = nu1+nu2+nu3+nu

    cursor5 = connection.cursor()
    cursor5.execute("SELECT COUNT(*) FROM a_page_сreate_e_naryad_table_1 INNER JOIN a_page_сreate_e_naryad_table_2 ON a_page_сreate_e_naryad_table_2.number_naryad = a_page_сreate_e_naryad_table_1.number_naryad INNER JOIN a_page_create_e_naryad_table_3 ON a_page_create_e_naryad_table_3.number_naryad = a_page_сreate_e_naryad_table_1.number_naryad INNER JOIN a_page_create_e_naryad_table_4 ON a_page_create_e_naryad_table_4.number_naryad = a_page_сreate_e_naryad_table_1.number_naryad WHERE a_page_сreate_e_naryad_table_1.organization_id = a_page_сreate_e_naryad_table_2.organization_id AND a_page_сreate_e_naryad_table_2.organization_id = a_page_create_e_naryad_table_3.organization_id AND a_page_create_e_naryad_table_3.organization_id = a_page_create_e_naryad_table_4.organization_id AND a_page_сreate_e_naryad_table_1.work_manager_id = a_page_сreate_e_naryad_table_2.responsible_manager_id AND a_page_сreate_e_naryad_table_2.responsible_manager_id = a_page_create_e_naryad_table_3.responsible_manager_id AND a_page_create_e_naryad_table_3.responsible_manager_id = a_page_create_e_naryad_table_4.responsible_manager_id")
    number5 = dictfetchone(cursor5)
    nu5 = number5[0]

    context={'nu':nu, 'nu1':nu1,'nu2':nu2,'nu3':nu3,'nu4':nu4,'nu5':nu5}

    return render(request, 'enar.html', context)



@login_required(login_url='login')
def create_nar_page1(request):
    form = CreateNar1Form()
    

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = CreateNar1Form(request.POST, request.FILES)
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
        form = CreateNar2Form(request.POST, request.FILES)
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
        form = CreateNar3Form(request.POST, request.FILES)
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
        form = CreateNar4Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('enar')


    context={'form':form}
    return render(request, 'create_nar_page4.html', context)

@login_required(login_url='login')
def archive(request):

    return render(request, 'archive.html')

@login_required(login_url='login')
def mainpage(request):

    return render(request, 'mainpage.html')

@login_required(login_url='login')
def open_nar_page1(request):

    openNar1 = сreate_e_naryad_table_1.objects.all()
    openNar2 = сreate_e_naryad_table_2.objects.all()
    openNar3 = create_e_naryad_table_3.objects.all()
    openNar4 = create_e_naryad_table_4.objects.all()
    
    context={'openNar1':openNar1, 'openNar2':openNar2, 'openNar3':openNar3, 'openNar4':openNar4}
    
    return render(request, 'open_nar_page1.html', context)



@login_required(login_url='login')
def close_nar_page1(request):
    return render(request, 'close_nar_page1.html')

@login_required(login_url='login')
def show_nar_page1(request, pk):
    showNar = сreate_e_naryad_table_1.objects.filter(id=pk)
    

    context={'showNar':showNar}

    return render(request, 'showNar1.html', context)

@login_required(login_url='login')
def show_nar_page2(request, pk):
    showNar = сreate_e_naryad_table_2.objects.filter(id=pk)
    

    context={'showNar':showNar}

    return render(request, 'showNar2.html', context)


@login_required(login_url='login')
def show_nar_page3(request, pk):
    showNar = create_e_naryad_table_3.objects.filter(id=pk)
    

    context={'showNar':showNar}

    return render(request, 'showNar3.html', context)


@login_required(login_url='login')
def show_nar_page4(request, pk):
    showNar = create_e_naryad_table_4.objects.filter(id=pk)
    

    context={'showNar':showNar}

    return render(request, 'showNar4.html', context)

@login_required(login_url='login')
def order_index(request):

    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM a_page_order")
    # orders = dictfetchall(cursor)

    # print(orders)
    # print(connection.queries)
    orders = Order.objects.all()
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
    cursor = connection.cursor()
    cursor.execute("SELECT id,user_id, username, password, name, surname, position FROM a_page_employee ")
    employee = dictfetchall(cursor)
    
    context={'employee':employee}
    return render(request, 'employee_list.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def employee(request,pk_test):
    cursor = connection.cursor()
    cursor.execute("SELECT user_id, username_id, profile_pic,user_id,name, surname, position, username, profile_pic, emp_h_at_work, holiday_h, sick_h FROM a_page_employee INNER JOIN a_page_employee_time ON a_page_employee_time.username_id = a_page_employee.id WHERE a_page_employee_time.username_id = '%s'" % pk_test)
    employee = dictfetchall(cursor)

    
    context={'employee':employee}
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