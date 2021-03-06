# Generated by Django 2.2.5 on 2020-02-02 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RepairInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repairTitle', models.CharField(max_length=10, verbose_name='报修标题')),
                ('repairContent', models.TextField(verbose_name='报修内容')),
                ('repairTime', models.DateTimeField(auto_now=True, verbose_name='报修时间')),
                ('repairStatus', models.CharField(choices=[('0', '未处理'), ('1', '待反馈')], default=0, max_length=1, verbose_name='报修状态')),
                ('repairName', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='报修姓名')),
            ],
            options={
                'verbose_name': '维修信息',
                'verbose_name_plural': '维修信息',
            },
        ),
        migrations.CreateModel(
            name='CostInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('0', '水费'), ('1', '电费'), ('2', '燃气费'), ('3', '物业管理费')], max_length=1, verbose_name='费用类型')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='金额')),
                ('costStatus', models.CharField(choices=[('0', '待缴纳'), ('1', '已缴纳')], default=0, max_length=1, verbose_name='缴费状态')),
                ('startTime', models.DateField(verbose_name='起始时间')),
                ('endTime', models.DateField(verbose_name='终止时间')),
                ('accountOwner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='居民姓名')),
            ],
            options={
                'verbose_name': '费用信息',
                'verbose_name_plural': '费用信息',
            },
        ),
    ]
