# Generated by Django 3.1 on 2020-08-14 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='ssn',
            field=models.CharField(max_length=9),
        ),
    ]