from django.db import models
    
class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    
class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dosage= models.FloatField()
    desc = models.CharField(max_length=200)
    quantity = models.FloatField()
    import_date = models.DateField()
    expiry = models.DateField()
    import_no = models.IntegerField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, default=None)