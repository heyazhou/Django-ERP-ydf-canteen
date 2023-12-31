# Generated by Django 3.0.7 on 2020-06-15 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basedata', '0002_auto_20200615_1024'),
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='invoice', verbose_name='invoice file'),
        ),
        migrations.AlterField(
            model_name='poitem',
            name='material',
            field=models.ForeignKey(limit_choices_to={'is_virtual': '0'}, on_delete=django.db.models.deletion.CASCADE, to='basedata.Material', verbose_name='material'),
        ),
        migrations.AlterField(
            model_name='poitem',
            name='tax',
            field=models.CharField(choices=[], default='0.00', max_length=6, verbose_name='tax rate'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='attach',
            field=models.FileField(blank=True, help_text='您可导入采购明细，模板请参考文档FD0008', null=True, upload_to='', verbose_name='attach'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='partner',
            field=models.ForeignKey(limit_choices_to={'partner_type': 'S'}, on_delete=django.db.models.deletion.CASCADE, to='basedata.Partner', verbose_name='partner'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(choices=[('0', 'NEW'), ('1', 'IN PROGRESS'), ('4', 'DROP'), ('9', 'APPROVED'), ('99', 'ALREADY STOCK IN')], default='0', max_length=2, verbose_name='status'),
        ),
    ]
