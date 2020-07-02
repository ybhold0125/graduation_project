from django.db import models
from CommunityPersonnel.models import User


class CostInfo(models.Model):
    accountOwner = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='costInfo',
        verbose_name="居民姓名"
    )

    Type = (
        (0, u'水费'),
        (1, u'电费'),
        (2, u'燃气费'),
        (3, u'物业管理费'),
    )

    type = models.IntegerField(
        choices=Type,
        verbose_name="费用类型"
    )

    costTitle = models.CharField(
        max_length=20,
        verbose_name="费用名称"
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="金额"
    )

    Status = (
        (0, u'待缴纳'),
        (1, u'已缴纳'),
    )

    costStatus = models.IntegerField(
        choices=Status,
        default=0,
        verbose_name="缴费状态"
    )

    startTime = models.DateField(
        auto_now_add=True,
        verbose_name="起始时间"
    )

    endTime = models.DateField(
        verbose_name="终止时间"
    )

    def __str__(self):
        return '%s' % self.accountOwner

    class Meta:
        verbose_name="费用信息"
        verbose_name_plural = verbose_name


class RepairInfo(models.Model):
    repairName = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='repairInfo',
        verbose_name="报修姓名"
    )

    repairTitle = models.CharField(
        max_length=20,
        verbose_name="报修标题"
    )

    repairNote = models.TextField(
        verbose_name="报修备注"
    )

    repairPhone = models.CharField(
        max_length=11,
        verbose_name="联系电话"
    )

    repairTime = models.DateTimeField(
        auto_now_add=True,
        verbose_name="报修时间"
    )

    Status = (
        (0, u'未处理'),
        (1, u'待反馈'),
    )

    repairStatus = models.IntegerField(
        choices=Status,
        default=0,
        verbose_name="报修状态"
    )

    def __str__(self):
        return '%s' % self.repairName

    class Meta:
        verbose_name = "维修信息"
        verbose_name_plural = verbose_name


class FeedbackInfo(models.Model):
    feedbackName = models.ForeignKey(
        User,
        verbose_name="反馈人",
        related_name='feedbackInfo',
        on_delete=models.CASCADE
    )

    feedbackTitle = models.CharField(
        max_length=15,
        verbose_name="反馈标题"
    )

    feedbackContent = models.TextField(
        verbose_name="反馈内容"
    )

    feedbackContact = models.CharField(
        max_length=15,
        verbose_name="QQ/邮箱(选填)",
        null=True,
        blank=True
    )

    feedbackTime = models.DateTimeField(
        auto_now_add=True,
        verbose_name="反馈时间"
    )

    def __str__(self):
        return '%s' % self.feedbackTitle

    class Meta:
        verbose_name = "反馈信息"
        verbose_name_plural = verbose_name


class MessageBoard(models.Model):
    messageName = models.ForeignKey(
        User,
        verbose_name="留言人",
        on_delete=models.CASCADE
    )
    messageContent = models.TextField(
        verbose_name="留言内容",
    )
    messageNickname = models.CharField(
        max_length=10,
        verbose_name="留言昵称"
    )
    messageTime = models.DateTimeField(
        auto_now_add=True,
        verbose_name="留言时间"
    )

    def __str__(self):
        return '%s' % self.messageNickname

    class Meta:
        ordering = ('-messageTime',)
        verbose_name = "留言板"
        verbose_name_plural = verbose_name