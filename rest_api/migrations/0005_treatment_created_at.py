# Generated by Django 4.2.4 on 2023-08-26 15:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0004_diagnosis_medication_remove_treatment_hours_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
