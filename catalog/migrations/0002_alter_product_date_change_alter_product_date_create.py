# Generated by Django 4.2.4 on 2023-09-09 08:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_change',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 9, 8, 44, 39, 767531, tzinfo=datetime.timezone.utc), verbose_name='дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 9, 8, 44, 39, 767531, tzinfo=datetime.timezone.utc), verbose_name='дата создания'),
        ),
    ]
