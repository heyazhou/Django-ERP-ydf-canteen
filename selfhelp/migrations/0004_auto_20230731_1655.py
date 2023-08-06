# Generated by Django 3.0.7 on 2023-07-31 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfhelp', '0003_auto_20211208_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='business_domain',
            field=models.CharField(choices=[], default='OT', max_length=4, verbose_name='business domain'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='classification',
            field=models.CharField(choices=[('S', '内部服务'), ('R', '设备维修'), ('Q', '问题咨询'), ('D', '采购申请')], default='D', max_length=4, verbose_name='classification'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='status',
            field=models.CharField(blank=True, choices=[], default='NEW', max_length=6, null=True, verbose_name='status'),
        ),
    ]