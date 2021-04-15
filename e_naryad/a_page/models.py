from django.db import models

# Create your models here.

class Employee(models.Model):
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name  

class Employee_Time(models.Model):
    username = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    emp_h_at_work = models.BigIntegerField(null=True)
    holiday_h = models.BigIntegerField(null=True)
    sick_h = models.BigIntegerField(null=True)

class ChangeNames(models.Model):
    organization = models.CharField(max_length=200, null=True)
    plot = models.CharField(max_length=200, null=True)
    admitting = models.CharField(max_length=200, null=True)
    team_members = models.CharField(max_length=200, null=True)
    category_of_work = models.CharField(max_length=200, null=True)
    subdivision = models.CharField(max_length=200, null=True)
    work_manager = models.CharField(max_length=200, null=True)
    manufacturer_work_manager = models.CharField(max_length=200, null=True)
    to_observer = models.CharField(max_length=200, null=True)
    entrusted = models.CharField(max_length=200, null=True)
    briefing_carried = models.CharField(max_length=200, null=True)
    briefing_carried1 = models.CharField(max_length=200, null=True)
    an_object = models.CharField(max_length=200, null=True)
    received_briefing = models.CharField(max_length=200, null=True)
    received_briefing1 = models.CharField(max_length=200, null=True)

class create_e_naryad_table_1(models.Model):
    organization = models.ForeignKey(ChangeNames, null=True, on_delete=models.SET_NULL)
    plot = models.ForeignKey(ChangeNames, null=True, on_delete=models.SET_NULL)
    admitting = models.ForeignKey(ChangeNames, null=True, on_delete=models.SET_NULL)
    team_members = models.ManyToManyField(ChangeNames)
    category_of_work = models.ForeignKey(ChangeNames, null=True, on_delete=models.SET_NULL)
    employee_preparedness_time = models.DateField()
    start_work = models.DateField()
    finish_work = models.DateField()
    subdivision = models.ForeignKey(ChangeNames, null=True, on_delete=models.SET_NULL)
    work_manager = models.ForeignKey(ChangeNames, null=True, on_delete=models.SET_NULL)
    manufacturer_work_manager = models.ForeignKey(ChangeNames, null=True, on_delete=models.SET_NULL)
    to_observer = models.ForeignKey(ChangeNames, null=True, on_delete=models.SET_NULL)
    entrusted = models.ForeignKey(ChangeNames, null=True, on_delete=models.SET_NULL)
    an_object = models.ForeignKey(ChangeNames, null=True, on_delete=models.SET_NULL)
    workplace_preparation_text1 = models.TextField()
    workplace_preparation_text2 = models.TextField()
    workplace_preparation_text3 = models.TextField()
    name = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    surname = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    username = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)




    



