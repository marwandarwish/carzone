# Generated by Django 5.1.2 on 2024-10-17 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('car_id', models.CharField(max_length=50)),
                ('customer_need', models.CharField(max_length=50)),
                ('car_title', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
            ],
        ),
    ]
