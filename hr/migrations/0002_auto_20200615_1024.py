# Generated by Django 3.0.7 on 2020-06-15 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeesalaryitem',
            name='calculate_way',
            field=models.CharField(choices=[], default='10', max_length=2, verbose_name='calculate way'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='category',
            field=models.CharField(blank=True, choices=[], default='21', max_length=2, null=True, verbose_name='employ category'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='gender',
            field=models.CharField(choices=[], default='1', max_length=2, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='probation_months',
            field=models.CharField(choices=[], default='3', max_length=2, verbose_name='probation months'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='profile',
            field=models.FileField(blank=True, null=True, upload_to='hr profile', verbose_name='profile'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='rank',
            field=models.CharField(choices=[], default='00', max_length=2, verbose_name='employee rank'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='ygxs',
            field=models.CharField(blank=True, choices=[], default='2', max_length=2, null=True, verbose_name='employ ygxs'),
        ),
        migrations.AlterField(
            model_name='salaryitem',
            name='classification',
            field=models.CharField(choices=[], default='10', max_length=2, verbose_name='classification'),
        ),
        migrations.AlterField(
            model_name='salaryitem',
            name='plus_or_minus',
            field=models.CharField(choices=[], default='+', max_length=2, verbose_name='plus or minus'),
        ),
    ]
