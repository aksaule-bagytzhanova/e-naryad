from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name  




