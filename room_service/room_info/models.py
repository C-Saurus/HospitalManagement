from django.db import models

# Create your models here.
class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    bed_number = models.IntegerField()
    
class Bed(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    department_id = models.IntegerField()
    price = models.FloatField()

class Clinic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    department_id = models.IntegerField()
    header_id = models.IntegerField()