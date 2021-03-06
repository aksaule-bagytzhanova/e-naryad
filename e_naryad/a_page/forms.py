from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Employee, Order, сreate_e_naryad_table_1, сreate_e_naryad_table_2, create_e_naryad_table_3, create_e_naryad_table_4
from django.core import validators

from django import forms

class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        exclude=['user']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['number_naryad', 'technical_activities', 'place_name_work', 'work_supervisor', 'team_members', 'person_give_naryad', 'started_work', 'work_done']
        widgets = {
            'number_naryad': widgets.NumberInput(attrs={'class':'form-control'}),
            'technical_activities': widgets.TextInput(attrs={'class':'form-control'}),
            'place_name_work': widgets.TextInput(attrs={'class':'form-control'}),
            'work_supervisor': widgets.Select(attrs={'class':'form-control select2'}),
            'team_members': widgets.SelectMultiple(attrs={'class':"form-control select2 selectpicker", 'multiple data-live-search':"true"}),
            'person_give_naryad': widgets.Select(attrs={'class':'form-control select2'}),
            'started_work': widgets.DateInput(attrs={'class':'form-control','id':"start_date", 'placeholder':"Date", 'type':"date"}),
            'work_done':  widgets.DateInput(attrs={'class':'form-control' ,'id':"start_date", 'placeholder':"Date", 'type':"date"})

        }

class CreateNar1Form(ModelForm):
    class Meta:
        model = сreate_e_naryad_table_1
        fields = ['number_naryad', 'organization', 'plot', 'admitting', 'team_members', 'category_of_work', 'emergency_preparedness_time', 'object', 'finish_work', 'name_electrical', 'separate_instructions', 'signature', 'subdivision', 'work_manager', 'manufacturer', 'observer', 'single_line_diagram', 'entrusted', 'start_work', 'disconnected_where', 'enar_give']
        widgets = {
            'number_naryad': widgets.NumberInput(attrs={'class':'form-control'}),
            'organization': widgets.Select(attrs={'class':'form-control select2'}),
            'plot': widgets.Select(attrs={'class':'form-control select2'}),
            'admitting': widgets.Select(attrs={'class':'form-control select2'}),
            'team_members': widgets.SelectMultiple(attrs={'class':"form-control select2 selectpicker", 'multiple data-live-search':"true"}),
            'category_of_work': widgets.Select(attrs={'class':'form-control select2'}),
            'emergency_preparedness_time': widgets.DateInput(attrs={'class':'form-control','id':"start_date", 'placeholder':"Date", 'type':"date"}),
            'object': widgets.Select(attrs={'class':'form-control select2'}),
            'finish_work':  widgets.DateInput(attrs={'class':'form-control' ,'id':"start_date", 'placeholder':"Date", 'type':"date"}),
            'name_electrical':widgets.Textarea(attrs={'class':'form-control', 'rows':'3', 'style':'margin-top: 0px; margin-bottom: 0px; height: 60px; width: 100%;'}),
            'separate_instructions': widgets.Textarea(attrs={'class':'form-control', 'rows':'3', 'style':'margin-top: 0px; margin-bottom: 0px; height: 60px; width: 100%;'}),
            'signature': widgets.FileInput(attrs={'class':'form-control custom-file', 'type':'file'}),
            'subdivision': widgets.Select(attrs={'class':'form-control select2'}),
            'work_manager': widgets.Select(attrs={'class':'form-control select2'}),
            'manufacturer': widgets.Select(attrs={'class':'form-control select2'}),
            'observer': widgets.Select(attrs={'class':'form-control select2'}),
            'single_line_diagram': widgets.FileInput(attrs={'class':'form-control custom-file', 'type':'file'}),
            'entrusted': widgets.Select(attrs={'class':'form-control select2'}),
            'start_work': widgets.DateInput(attrs={'class':'form-control' ,'id':"start_date", 'placeholder':"Date", 'type':"date"}),
            'disconnected_where': widgets.Textarea(attrs={'class':'form-control', 'rows':'3', 'style':'margin-top: 0px; margin-bottom: 0px; height: 60px; width: 100%;'}),
            'enar_give': widgets.Select(attrs={'class':'form-control select2'})
        }


class CreateNar2Form(ModelForm):
    class Meta:
        model = сreate_e_naryad_table_2
        fields = ['number_naryad', 'enar_give', 'signature_enar_give', 'responsible_manager', 'signature_responsible_manager', 'organization']
        widgets = {
            'number_naryad': widgets.NumberInput(attrs={'class':'form-control'}),
            'organization': widgets.Select(attrs={'class':'form-control select2'}),
            'enar_give': widgets.Select(attrs={'class':'form-control select2'}),
            'signature_enar_give': widgets.FileInput(attrs={'class':'form-control custom-file', 'type':'file'}),
            'responsible_manager': widgets.Select(attrs={'class':'form-control select2'}),
            'signature_responsible_manager': widgets.FileInput(attrs={'class':'form-control custom-file', 'type':'file'})
            
        }

class CreateNar3Form(ModelForm):
    class Meta:
        model = create_e_naryad_table_3
        fields = ['number_naryad', 'enar_give', 'signature_enar_give', 'date_time', 'workplaces_prepared', 'agreed', 'admitting', 'responsible_manager', 'organization']
        widgets = {
            'number_naryad': widgets.NumberInput(attrs={'class':'form-control'}),
            'enar_give': widgets.Select(attrs={'class':'form-control select2'}),
            'signature_enar_give': widgets.FileInput(attrs={'class':'form-control custom-file', 'type':'file'}),
            'date_time': widgets.DateInput(attrs={'class':'form-control' ,'id':"start_date", 'placeholder':"Date", 'type':"date"}),
            'workplaces_prepared': widgets.Textarea(attrs={'class':'form-control', 'rows':'3', 'style':'margin-top: 0px; margin-bottom: 0px; height: 126px; width: 100%;'}),
            'agreed': widgets.TextInput(attrs={'class':'form-control'}),
            'admitting': widgets.Select(attrs={'class':'form-control select2'}),
            'responsible_manager': widgets.Select(attrs={'class':'form-control select2'}),
            'organization': widgets.Select(attrs={'class':'form-control select2'})
        }

class CreateNar4Form(ModelForm):
    class Meta:
        model = create_e_naryad_table_4
        fields = ['number_naryad', 'reported', 'manufacturer', 'responsible_manager', 'admitting', 'signature_manufacturer', 'signature_responsible_manager', 'signature_admitting', 'organization']
        widgets = {
            'number_naryad': widgets.NumberInput(attrs={'class':'form-control'}),
            'reported': widgets.TextInput(attrs={'class':'form-control'}),
            'manufacturer': widgets.Select(attrs={'class':'form-control select2'}),
            'responsible_manager': widgets.Select(attrs={'class':'form-control select2'}),
            'admitting': widgets.Select(attrs={'class':'form-control select2'}),
            'signature_manufacturer':widgets.FileInput(attrs={'class':'form-control custom-file', 'type':'file'}),
            'signature_responsible_manager': widgets.FileInput(attrs={'class':'form-control custom-file', 'type':'file'}),
            'signature_admitting': widgets.FileInput(attrs={'class':'form-control custom-file', 'type':'file'}),
            'organization': widgets.Select(attrs={'class':'form-control select2'})
        }