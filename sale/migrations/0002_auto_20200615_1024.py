# Generated by Django 3.0.7 on 2020-06-15 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basedata', '0002_auto_20200615_1024'),
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offeritem',
            name='material',
            field=models.ForeignKey(blank=True, limit_choices_to={'can_sale': '1', 'is_virtual': '0'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedata.Material', verbose_name='material'),
        ),
        migrations.AlterField(
            model_name='offeritem',
            name='tax',
            field=models.CharField(choices=[], default='0.00', max_length=6, verbose_name='tax rate'),
        ),
        migrations.AlterField(
            model_name='offersheet',
            name='attach',
            field=models.FileField(blank=True, help_text='您可导入报价明细，模板请参考文档FD0006', null=True, upload_to='offer sheet', verbose_name='offer sheet file'),
        ),
        migrations.AlterField(
            model_name='offersheet',
            name='partner',
            field=models.ForeignKey(limit_choices_to={'partner_type': 'C'}, on_delete=django.db.models.deletion.CASCADE, to='basedata.Partner', verbose_name='partner'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='material',
            field=models.ForeignKey(blank=True, limit_choices_to={'can_sale': '1', 'is_virtual': '0'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedata.Material', verbose_name='material'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='tax',
            field=models.CharField(choices=[], default='0.00', max_length=6, verbose_name='tax rate'),
        ),
        migrations.AlterField(
            model_name='saleorder',
            name='invoice_type',
            field=models.CharField(choices=[], default='10', max_length=6, verbose_name='invoice type'),
        ),
        migrations.AlterField(
            model_name='saleorder',
            name='partner',
            field=models.ForeignKey(limit_choices_to={'partner_type': 'C'}, on_delete=django.db.models.deletion.CASCADE, to='basedata.Partner', verbose_name='partner'),
        ),
        migrations.AlterField(
            model_name='saleorder',
            name='status',
            field=models.CharField(choices=[('0', 'NEW'), ('1', 'IN PROGRESS'), ('4', 'DROP'), ('9', 'APPROVED'), ('99', 'ALREADY STOCK OUT')], default='0', max_length=2, verbose_name='status'),
        ),
    ]
