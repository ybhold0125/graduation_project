# Generated by Django 2.2.5 on 2020-02-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InformationModule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costinfo',
            name='startTime',
            field=models.DateField(auto_now=True, verbose_name='起始时间'),
        ),
    ]
