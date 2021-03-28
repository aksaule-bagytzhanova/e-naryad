from django.urls import path
from . import views

urlpatterns = [
    path('', views.enar,name='enar'),
    path('page', views.page1),
    path('create_nar', views.create_nar_page1, name='create_nar_page1'),
    path('open_nar', views.open_nar_page1, name='open_nar_page1'),
    path('close_nar', views.close_nar_page1, name='close_nar_page1'),
    path('order_index', views.order_index, name='order_index'),
    
    
]