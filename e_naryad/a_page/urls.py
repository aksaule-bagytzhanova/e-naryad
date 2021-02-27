from django.urls import path
from . import views

urlpatterns = [
    path('', views.enar),
    path('page', views.page1),
    
]