from django.db import models

# Create your models here.
class Fullname(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    mid_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
class Status(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    
class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
        
class Address(models.Model):
    id = models.AutoField(primary_key=True)
    no_house = models.IntegerField()
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    
class Relatives(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    
class RentInfo(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField(default=None, null=True)
    bed_id = models.IntegerField()
    price = models.FloatField(default=None, null=True)
    patient_id = models.IntegerField()

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.ForeignKey(Fullname, on_delete=models.CASCADE)
    age = models.IntegerField()
    dob = models.DateField()
    cccd = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    address = models.ForeignKey(Address, on_delete=models.CASCADE) 
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    relatives = models.ForeignKey(Relatives, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=None)