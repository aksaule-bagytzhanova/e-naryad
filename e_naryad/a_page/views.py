from django.shortcuts import render

# Create your views here.
def page1(request):
    return render(request, 'page1.html')

def enar(request):
    return render(request, 'enar.html')

def create_nar_page1(request):
    return render(request, 'create_nar_page1.html')

def open_nar_page1(request):
    return render(request, 'open_nar_page1.html')

def close_nar_page1(request):
    return render(request, 'close_nar_page1.html')

def order_index(request):
    return render(request, 'order/order_index.html') 

def order_edit(request):
    return render(request, 'order/order_edit.html')

def order_add(request):
    return render(request, 'order/order_add.html')


