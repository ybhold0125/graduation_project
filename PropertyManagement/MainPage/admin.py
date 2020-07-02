from django.contrib import admin
from .models import News, SwipePicture, Announcement


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'news_title', 'news_time')


@admin.register(SwipePicture)
class SwipePictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'picture')


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'announcement_detail', 'announcement_time')