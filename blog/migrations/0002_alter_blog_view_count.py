# Generated by Django 4.2.4 on 2023-09-16 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='view_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='количество просмотров'),
        ),
    ]
