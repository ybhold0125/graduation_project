# Generated by Django 2.2 on 2020-04-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppletRelated', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appletrelated',
            options={'ordering': ('-id',), 'verbose_name': '程序版本信息', 'verbose_name_plural': '程序版本信息'},
        ),
        migrations.AlterField(
            model_name='appletrelated',
            name='updateTime',
            field=models.DateField(auto_now_add=True, verbose_name='更新时间'),
        ),
    ]
