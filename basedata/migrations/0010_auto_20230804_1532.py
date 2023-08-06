# Generated by Django 3.0.7 on 2023-08-04 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basedata', '0009_auto_20230804_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='measure',
        ),
        migrations.AddField(
            model_name='material',
            name='measure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedata.Measure', verbose_name='measure'),
        ),
    ]
