from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.enar,name='enar'),
    path('page/', views.page1),
    path('create_nar/', views.create_nar_page1, name='create_nar_page1'),
    path('open_nar/', views.open_nar_page1, name='open_nar_page1'),
    path('close_nar/', views.close_nar_page1, name='close_nar_page1'),
    path('order_index/', views.order_index, name='order_i'),
    path('order_edit/<str:pk>/', views.order_edit, name='order_e'),
    path('order_add/', views.order_add, name='order_a'),
    path('passport/', views.passport_i, name = 'passport_i'),
    path('passport/cabel', views.passport_cabel, name = 'passport_cabel'),
    path('passport/circuit', views.passport_circuit, name = 'passport_circuit'),
    path('passport/distribution', views.passport_distribution, name = 'passport_distribution'), 
    path('passport/blade', views.passport_blade, name = 'passport_blade'), 
    path('passport/indoor', views.passport_indoor, name = 'passport_indoor'), 
    path('passport/isg', views.passport_isg, name = 'passport_isg'), 
    path('passport/list', views.passport_list, name = 'passport_list'), 
    path('passport/mcc', views.passport_mcc, name = 'passport_mcc'), 
    path('passport/motor', views.passport_motor, name = 'passport_motor'), 
    path('passport/panel', views.passport_panel, name = 'passport_panel'), 
    path('passport/pg', views.passport_pg, name = 'passport_pg'), 
    path('passport/substation', views.passport_substation, name = 'passport_substation'), 
    path('passport/uts', views.passport_uts, name = 'passport_uts'), 
    path('contact_us/', views.contact, name='contact'),
    path('calendar/', views.calendar, name ='calendar'),
    path('gate/', views.gate, name='gate'),
    path('gate/add_sick_days', views.add_sick, name='add_sick'),
    path('employee/<str:pk_test>/', views.employee, name='employee'),
    path('flexi_time', views.flexi_time, name='flexi_time'),
    path('add_holiday', views.add_holiday, name='add_holiday'),
    path('plan_index', views.plan_index, name='plan_index'),
    path('mess_index', views.messages_index, name='mess_index'),
    path('login/', views.login, name='login'),
    
    
    
    
]