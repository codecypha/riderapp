# Generated by Django 3.1.4 on 2021-02-26 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snappy', '0004_auto_20210226_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
