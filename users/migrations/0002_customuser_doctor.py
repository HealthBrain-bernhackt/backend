# Generated by Django 4.2.4 on 2023-08-26 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='doctor',
            field=models.BooleanField(default=False),
        ),
    ]
