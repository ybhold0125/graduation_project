# Generated by Django 2.2.5 on 2020-02-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommunityPersonnel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default=1, max_length=6, verbose_name='居民姓名'),
            preserve_default=False,
        ),
    ]