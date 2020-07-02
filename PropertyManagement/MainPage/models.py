from django.db import models


class SwipePicture(models.Model):
    picture = models.ImageField(
        upload_to='SwipePicture/',
        verbose_name="主页轮播图片"
    )

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name


class News(models.Model):
    news_title = models.CharField(
        max_length=50,
        verbose_name="新闻标题"
    )

    news_summary = models.CharField(
        max_length=255,
        verbose_name="新闻概述"
    )

    news_time = models.CharField(
        max_length=10,
        verbose_name="新闻时间"
    )

    news_detail = models.TextField(
        verbose_name="新闻内容"
    )

    def __str__(self):
        return self.news_title

    class Meta:
        ordering = ('-news_time',)
        verbose_name = "新闻栏"
        verbose_name_plural = verbose_name
        db_table = "news"


class Announcement(models.Model):
    announcement_detail = models.CharField(
        max_length=30,
        verbose_name="公告内容"
    )

    announcement_time = models.DateField(
        auto_now_add=True,
        verbose_name="公告时间"
    )

    def __str__(self):
        return self.announcement_detail

    class Meta:
        ordering = ('-id',)
        verbose_name = "公告栏"
        verbose_name_plural = verbose_name
