from djongo import models
    
class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.IntegerField()
    status = models.CharField(max_length=20)
    bhyt = models.BooleanField()
    medicine_record_id = models.IntegerField()
    
class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, default=None)
    pay_date = models.DateField()
    type = models.CharField(max_length=20)
    total_price = models.FloatField()
