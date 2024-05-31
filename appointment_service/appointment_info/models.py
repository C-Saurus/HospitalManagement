from djongo import models

# Create your models here.
    
class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    
class Status(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    date = models.DateTimeField()
    duration = models.FloatField()
    room = models.CharField(max_length=200)
    building = models.CharField(max_length=200)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=None)