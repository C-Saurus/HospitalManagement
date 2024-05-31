# Generated by Django 4.1.13 on 2024-05-31 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('patient_id', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('bhyt', models.BooleanField()),
                ('medicine_record_id', models.IntegerField()),
                ('total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pay_date', models.DateField()),
                ('type', models.CharField(max_length=20)),
                ('total_price', models.FloatField()),
                ('bill', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bill_info.bill')),
            ],
        ),
    ]
