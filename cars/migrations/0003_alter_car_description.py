# Generated by Django 5.1.2 on 2024-10-15 10:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20241015_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=5000),
        ),
    ]
