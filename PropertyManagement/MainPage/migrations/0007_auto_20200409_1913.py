# Generated by Django 2.2 on 2020-04-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0006_announcement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='announcement_time',
            field=models.DateField(verbose_name='公告时间'),
        ),
    ]
