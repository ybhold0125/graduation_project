# Generated by Django 2.2 on 2020-03-21 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InformationModule', '0004_feedbackinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='costinfo',
            name='costTitle',
            field=models.CharField(default=1, max_length=20, verbose_name='费用名称状态'),
            preserve_default=False,
        ),
    ]
