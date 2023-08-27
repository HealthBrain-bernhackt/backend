# Generated by Django 4.2.4 on 2023-08-26 21:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0010_diagnosis_doctor_diagnosis_patient_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.CharField(default='Paediatrician', max_length=128),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='finish_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 2, 21, 25, 9, 315942, tzinfo=datetime.timezone.utc)),
        ),
    ]