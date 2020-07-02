# Generated by Django 2.2 on 2020-04-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InformationModule', '0012_auto_20200406_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costinfo',
            name='startTime',
            field=models.DateField(auto_now_add=True, verbose_name='起始时间'),
        ),
        migrations.AlterField(
            model_name='feedbackinfo',
            name='feedbackTime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='反馈时间'),
        ),
        migrations.AlterField(
            model_name='messageboard',
            name='messageTime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='留言时间'),
        ),
        migrations.AlterField(
            model_name='repairinfo',
            name='repairTime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='报修时间'),
        ),
    ]