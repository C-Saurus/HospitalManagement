# Generated by Django 4.1.13 on 2024-06-01 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_info', '0002_rentinfo_rename_distric_address_district_item_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentinfo',
            name='end_date',
            field=models.DateField(default=None, null=True),
        ),
    ]
