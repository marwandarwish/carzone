# Generated by Django 5.1.2 on 2024-10-15 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_doors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_photo_5',
        ),
    ]
