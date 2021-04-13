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


class create_e_naryad_table_1(models.Model):
    ORGANIZATION = (
        ('КаражанбасМунай', 'КаражанбасМунай'),
        ('Мангистаумунайгаз', 'Мангистаумунайгаз'),
        ('Buzachi Operating', 'Buzachi Operating'),
        ('CASPI BITUM', 'CASPI BITUM'),
        ('КаракудукМунай', 'КаракудукМунай'),
        ('TOTAL E & P Dunga', 'TOTAL E & P Dunga'),
        ('Кен-Сары', 'Кен-Сары'),
        ('OMV Petrom S.A.', 'OMV Petrom S.A.'),
        ('КазМунайТениз', 'КазМунайТениз'),
        ('СП Арман', 'СП Арман'),
        ('ТОО Мангистауэнергомунай', 'ТОО Мангистауэнергомунай'), 
    )
    username = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    organization = models.CharField(max_length=200, null=True, choices=ORGANIZATION)
    plot = models.CharField(max_length=200, null=True)
    admitting = models.CharField(max_length=200, null=True)
    team_member = models.CharField(max_length=200, null=True)
    category_of_work = models.CharField(max_length=200, null=True)
    employee_preparedness_time = models.CharField(max_length=200, null=True)
    an_object = models.CharField(max_length=200, null=True)
    finish_work_date = models.CharField(max_length=200, null=True)
    subdivision = models.CharField(max_length=200, null=True)
    work_manager = models.CharField(max_length=200, null=True)
    observer = models.CharField(max_length=200, null=True)
    open_single_line_diagrem = models.CharField(max_length=200, null=True)
    is_entrusted = models.CharField(max_length=200, null=True)
    start_work = models.DateTimeField()
    names_electrical_installations = models.TextField()
    separate_instructions = models.TextField()
    signature = models.CharField(max_length=200, null=True)
    be_disconnected = models.TextField()
    outfit_issued = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)




