# Generated by Django 4.2.4 on 2023-08-26 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='hours',
            field=models.TextField(),
        ),
    ]