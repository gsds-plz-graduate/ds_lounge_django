# Generated by Django 4.1.3 on 2022-11-21 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name = 'CheckCourse',
            fields = [
                ('cid_int', models.IntegerField(primary_key = True, serialize = False)),
                ('cid', models.CharField(max_length = 255)),
                ('cname', models.CharField(blank = True, max_length = 255, null = True)),
                ('crd', models.IntegerField(blank = True, null = True)),
                ('yr_20', models.CharField(blank = True, max_length = 255, null = True)),
                ('yr_21', models.CharField(blank = True, max_length = 255, null = True)),
                ('yr_22', models.CharField(blank = True, max_length = 255, null = True)),
            ],
            options = {
                'db_table': 'check_course',
                'managed' : False,
            },
        ),
    ]