# Generated by Django 3.1.4 on 2021-02-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snappy', '0003_remove_driver_licence_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=15),
        ),
    ]