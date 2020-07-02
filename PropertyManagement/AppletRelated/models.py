from django.db import models


class AppletRelated(models.Model):
    versionNumber = models.CharField(
        max_length=5,
        help_text="格式：1.0.0",
        verbose_name="版本号"
    )

    updateInformation = models.TextField(
        verbose_name="更新信息"
    )

    updateTime = models.DateField(
        auto_now_add=True,
        verbose_name="更新时间"
    )

    def __str__(self):
        return '%s' % self.versionNumber

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = verbose_name = "程序版本信息"