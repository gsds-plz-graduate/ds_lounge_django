# Generated by Django 4.1.3 on 2022-11-23 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excelupload', '0006_alter_document_student_number'),
    ]

    operations = [
        migrations.AddField(
            model_name = 'document',
            name = 'paperTest',
            field = models.BooleanField(default = False),
        ),
    ]
