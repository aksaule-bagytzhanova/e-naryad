from django.shortcuts import render, redirect
from django.urls import path
from .models import *
from .forms import OrderForm

# Create your views here.
def page1(request):
    return render(request, 'page1.html')

def enar(request):
    employees = Employee.objects.all()
    
    return render(request, 'enar.html')

def create_nar_page1(request):
    return render(request, 'create_nar_page1.html')

def open_nar_page1(request):
    return render(request, 'open_nar_page1.html')

def close_nar_page1(request):
    return render(request, 'close_nar_page1.html')

def order_index(request):
    orders = Order.objects.all()

    context={'orders':orders}
    return render(request, 'order/order_index.html', context) 

def order_edit(request):
    form = OrderForm() 

    context={'form':form}
    return render(request, 'order/order_add.html', context)

def order_add(request):

    form = OrderForm()
    
    
    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context={'form':form}
    return render(request, 'order/order_add.html', context)

def passport_i(request):
    return render(request, 'passport/passport_index.html')

def passport_cabel(request):
    return render(request, 'passport/passport_cabel.html')

def passport_circuit(request):
    return render(request, 'passport/passport_circuit.html')

def passport_distribution(request):
    return render(request, 'passport/passport_distribution.html')

def passport_blade(request):
    return render(request, 'passport/passport_blade.html')

def passport_indoor(request):
    return render(request, 'passport/passport_indoor.html')

def passport_isg(request):
    return render(request, 'passport/passport_isg.html')

def passport_list(request):
    return render(request, 'passport/passport_list.html')

def passport_mcc(request):
    return render(request, 'passport/passport_mcc.html')

def passport_motor(request):
    return render(request, 'passport/passport_motor.html')

def passport_panel(request):
    return render(request, 'passport/passport_panel.html')

def passport_pg(request):
    return render(request, 'passport/passport_panel.html')

def passport_substation(request):
    return render(request, 'passport/passport_substation.html')

def passport_uts(request):
    return render(request, 'passport/passport_uts.html')

def contact(request):
    return render(request, 'attendance/contact.html')

def calendar(request):
    return render(request, 'attendance/calendar.html')

def gate(request):
    return render(request, 'attendance/gate.html')

def add_sick(request):
    return render(request, 'attendance/add_sick.html')

def employee(request, pk_test):
    employees = Employee.objects.filter(id=pk_test) 

    context = {'employees':employees}
    return render(request, 'employee.html', context)

def flexi_time(request):
    return render(request, 'attendance/flexi_time.html')

def add_holiday(request):
    return render(request, 'attendance/add_holiday.html')

def plan_index(request):
    return render(request, 'plan/plan_index.html')

def messages_index(request):
    return render(request, 'messages/mess_index.html')

