from django.contrib import admin
from .models import AppletRelated


@admin.register(AppletRelated)
class AppletRelatedAdmin(admin.ModelAdmin):
    list_display = ('versionNumber', 'updateTime')
