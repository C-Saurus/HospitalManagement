from django.db import models

# Create your models here.
class Fullname(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    mid_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    salary = models.FloatField()
    level = models.IntegerField()
    
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    no = models.CharField(max_length=20)
        
class Address(models.Model):
    id = models.AutoField(primary_key=True)
    no_house = models.IntegerField()
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.ForeignKey(Fullname, on_delete=models.CASCADE)
    age = models.IntegerField()
    dob = models.DateField()
    hire_date = models.DateField()
    cccd = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    address = models.ForeignKey(Address, on_delete=models.CASCADE) 
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level = models.IntegerField()