# Generated by Django 3.1.4 on 2021-02-26 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disptach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initiator', models.CharField(max_length=150)),
                ('pickup', models.CharField(max_length=150)),
                ('dropoff', models.CharField(max_length=150)),
                ('itemName', models.CharField(max_length=150)),
                ('quantity', models.CharField(max_length=150)),
                ('note', models.TextField(max_length=250)),
                ('reciever_name', models.CharField(max_length=150)),
                ('recievers_phone', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
