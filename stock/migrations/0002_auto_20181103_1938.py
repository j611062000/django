# Generated by Django 2.1 on 2018-11-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_info',
            name='closing_price_of_the_day',
            field=models.CharField(max_length=10),
        ),
    ]
