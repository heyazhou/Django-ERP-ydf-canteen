# Generated by Django 3.0.7 on 2023-08-04 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basedata', '0006_auto_20230804_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='measure',
        ),
        migrations.AddField(
            model_name='material',
            name='measure',
            field=models.ForeignKey(default='千克', on_delete=django.db.models.deletion.CASCADE, to='basedata.Measure', verbose_name='measure'),
        ),
    ]
