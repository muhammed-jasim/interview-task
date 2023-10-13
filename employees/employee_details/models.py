from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200,null=True) 
    emp_id = models.CharField(max_length=3,null=True) 
    email = models.EmailField(max_length=30, null=True)
    phone = models.CharField(max_length=10,null=True)