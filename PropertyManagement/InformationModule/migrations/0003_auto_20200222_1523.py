# Generated by Django 2.2.5 on 2020-02-22 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InformationModule', '0002_auto_20200202_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costinfo',
            name='accountOwner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='costInfo', to=settings.AUTH_USER_MODEL, verbose_name='居民姓名'),
        ),
        migrations.AlterField(
            model_name='repairinfo',
            name='repairName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repairInfo', to=settings.AUTH_USER_MODEL, verbose_name='报修姓名'),
        ),
    ]