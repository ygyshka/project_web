# Generated by Django 4.2.4 on 2023-09-30 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_remove_category_created_at_version'),
    ]

    operations = [

        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='versions'),
        ),
    ]
