# Generated by Django 2.1 on 2018-11-30 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20181103_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fifteen_mins_interval',
            name='price_of_the_interval',
            field=models.FloatField(default=0),
        ),
    ]