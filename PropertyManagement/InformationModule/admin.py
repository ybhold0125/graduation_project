from django.contrib import admin
from .models import CostInfo, RepairInfo, FeedbackInfo, MessageBoard


@admin.register(CostInfo)
class CostInfoAdmin(admin.ModelAdmin):
    list_display = ["accountOwner", "type", "costTitle", "amount", "costStatus", "startTime", "endTime"]


@admin.register(RepairInfo)
class CostInfoAdmin(admin.ModelAdmin):
    list_display = ["repairName", "repairTitle", "repairPhone", "repairTime", "repairStatus"]


@admin.register(FeedbackInfo)
class FeedbackInfoAdmin(admin.ModelAdmin):
    list_display = ["feedbackName", "feedbackTitle", "feedbackContact", "feedbackTime"]


@admin.register(MessageBoard)
class MessageBoardAdmin(admin.ModelAdmin):
    list_display = ["messageName", "messageNickname", "messageTime"]