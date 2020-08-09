# Generated by Django 3.1 on 2020-08-09 09:16

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('logsheet', '0004_auto_20200809_0721'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summaryDate', models.DateField(default=datetime.date.today)),
                ('signInCount', models.IntegerField(default=0)),
                ('signOutCount', models.IntegerField(default=0)),
                ('totalDuration', models.FloatField(default=0.0)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
