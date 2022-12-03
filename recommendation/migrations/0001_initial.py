# Generated by Django 4.1.3 on 2022-12-02 21:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('check', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name = 'Courses',
            fields = [
                ('cid', models.ForeignKey(db_column = 'cid', on_delete = django.db.models.deletion.CASCADE, primary_key = True, serialize = False, to = 'check.coursekey')),
                ('program', models.CharField(blank = True, max_length = 5, null = True)),
                ('cname', models.CharField(blank = True, max_length = 100, null = True)),
                ('avg_quota', models.FloatField(blank = True, null = True)),
                ('classification', models.CharField(blank = True, max_length = 5, null = True)),
                ('dept', models.CharField(blank = True, max_length = 255, null = True)),
                ('lang', models.CharField(blank = True, max_length = 50, null = True)),
                ('yr_sem', models.CharField(blank = True, max_length = 255, null = True)),
                ('last_yr_sem', models.CharField(max_length = 10)),
                ('notes', models.TextField(blank = True, null = True)),
            ],
            options = {
                'db_table': 'rec_courses',
                'managed' : False,
            },
        ),
        migrations.CreateModel(
            name = 'RecommendedResult',
            fields = [
                ('id', models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID')),
                ('cname', models.CharField(blank = True, max_length = 255, null = True)),
                ('program', models.CharField(blank = True, max_length = 5, null = True)),
                ('classification', models.CharField(blank = True, max_length = 5, null = True)),
                ('crd', models.IntegerField(blank = True, null = True)),
                ('dept', models.CharField(blank = True, max_length = 255, null = True)),
                ('lang', models.CharField(blank = True, max_length = 50, null = True)),
                ('yr_sem', models.CharField(blank = True, max_length = 255, null = True)),
                ('last_yr_sem', models.CharField(blank = True, max_length = 10, null = True)),
            ],
            options = {
                'db_table': 'rec_result',
                'managed' : False,
            },
        ),
    ]