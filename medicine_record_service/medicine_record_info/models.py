from django.db import models

# Create your models here.

class Treatment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    
class Prescription(models.Model):
    id = models.AutoField(primary_key=True)
    medicine_id = models.IntegerField()
    quantity = models.FloatField()
    price = models.FloatField(default=None, null=True)
    treatment = models.ForeignKey(Treatment, related_name='prescriptions', on_delete=models.CASCADE, default=None)

class Dianosis(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    department_id = models.IntegerField()
    visit_date = models.DateField()
    note = models.CharField(max_length=200)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    dianosis = models.ForeignKey(Dianosis, on_delete=models.CASCADE, default=None)