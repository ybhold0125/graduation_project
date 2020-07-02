# Generated by Django 2.2 on 2020-03-31 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InformationModule', '0005_costinfo_costtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costinfo',
            name='costStatus',
            field=models.IntegerField(choices=[(0, '待缴纳'), (1, '已缴纳')], default=0, max_length=1, verbose_name='缴费状态'),
        ),
        migrations.AlterField(
            model_name='costinfo',
            name='type',
            field=models.IntegerField(choices=[(0, '水费'), (1, '电费'), (2, '燃气费'), (3, '物业管理费')], max_length=1, verbose_name='费用类型'),
        ),
        migrations.AlterField(
            model_name='repairinfo',
            name='repairStatus',
            field=models.IntegerField(choices=[(0, '未处理'), (1, '待反馈')], default=0, max_length=1, verbose_name='报修状态'),
        ),
    ]
