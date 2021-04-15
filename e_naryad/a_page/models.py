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

class Organization(models.Model):
    name = models.CharField(max_length=200)

class Plot(models.Model):
    name = models.CharField(max_length=200)

class Admitting(models.Model):
    name = models.CharField(max_length=200)

class Team_members(models.Model):
    name = models.CharField(max_length=200)

class Category_of_work(models.Model):
    name = models.CharField(max_length=200)

class Subdivision(models.Model):
    name = models.CharField(max_length=200)

class Work_manager(models.Model):
    name = models.CharField(max_length=200)

class Manufacturer_work_manager(models.Model):
    name = models.CharField(max_length=200)

class To_observer(models.Model):
    name = models.CharField(max_length=200)

class Entrusted(models.Model):
    name = models.CharField(max_length=200)

class An_object(models.Model):
    name = models.CharField(max_length=200)


class create_e_naryad_table_1(models.Model):
    organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)
    plot = models.ForeignKey(Plot, null=True, on_delete=models.SET_NULL)
    admitting = models.ForeignKey(Admitting, null=True, on_delete=models.SET_NULL)
    team_members = models.ManyToManyField(Team_members)
    category_of_work = models.ForeignKey(Category_of_work, null=True, on_delete=models.SET_NULL)
    employee_preparedness_time = models.DateField()
    start_work = models.DateField()
    finish_work = models.DateField()
    subdivision = models.ForeignKey(Subdivision, null=True, on_delete=models.SET_NULL)
    work_manager = models.ForeignKey(Work_manager, null=True, on_delete=models.SET_NULL)
    manufacturer_work_manager = models.ForeignKey(Manufacturer_work_manager, null=True, on_delete=models.SET_NULL)
    to_observer = models.ForeignKey(To_observer, null=True, on_delete=models.SET_NULL)
    entrusted = models.ForeignKey(Entrusted, null=True, on_delete=models.SET_NULL)
    an_object = models.ForeignKey(An_object, null=True, on_delete=models.SET_NULL)
    workplace_preparation_text1 = models.TextField()
    workplace_preparation_text2 = models.TextField()
    workplace_preparation_text3 = models.TextField()
    username = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)




    



