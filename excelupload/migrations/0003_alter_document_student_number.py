# Generated by Django 4.1.3 on 2022-11-21 17:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excelupload', '0002_alter_document_student_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name = 'document',
            name = 'student_number',
            field = models.CharField(max_length = 10, validators = [django.core.validators.RegexValidator(regex = '20\\d{2}-\\d{5}/')]),
        ),
    ]