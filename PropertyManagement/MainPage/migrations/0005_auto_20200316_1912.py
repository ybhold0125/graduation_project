# Generated by Django 2.2 on 2020-03-16 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0004_auto_20200316_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='SwipePicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='SwipePicture/', verbose_name='主页轮播图片')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-news_time',), 'verbose_name': '新闻栏', 'verbose_name_plural': '新闻栏'},
        ),
    ]
