# Generated by Django 4.1.3 on 2022-12-03 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_profile_uploaded_at_alter_profile_passed'),
    ]

    operations = [
        migrations.AddField(
            model_name = 'profile',
            name = 'include_undergrad',
            field = models.BooleanField(default = False),
        ),
    ]
