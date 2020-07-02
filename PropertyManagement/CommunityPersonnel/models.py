from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(
        max_length=6,
        verbose_name="居民姓名"
    )

    Sex = (
        (1, u'男'),
        (2, u'女'),
    )

    sex = models.IntegerField(
        choices=Sex,
        verbose_name="性别"
    )

    idNum = models.CharField(
        max_length=18,
        verbose_name="身份证号"
    )

    telephone = models.CharField(
        max_length=11,
        verbose_name="居民电话"
    )

    Type = (
        (1, u'140m²'),
        (2, u'120m²'),
        (3, u'100m²'),
    )

    unitType = models.IntegerField(
        choices=Type,
        verbose_name="户型"
    )

    address = models.CharField(
        max_length=7,
        help_text="栋-门牌号，例如9-1301",
        verbose_name="门牌号"
    )

    def __str__(self):
        return '%s' % self.name
    
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
