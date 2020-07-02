# Generated by Django 3.0.3 on 2020-03-01 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('InformationModule', '0003_auto_20200222_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedbackTitle', models.CharField(max_length=15, verbose_name='反馈标题')),
                ('feedbackContent', models.TextField(verbose_name='反馈内容')),
                ('feedbackTime', models.DateTimeField(auto_now=True, verbose_name='反馈时间')),
                ('feedbackName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbackInfo', to=settings.AUTH_USER_MODEL, verbose_name='反馈人')),
            ],
            options={
                'verbose_name': '反馈信息',
                'verbose_name_plural': '反馈信息',
            },
        ),
    ]