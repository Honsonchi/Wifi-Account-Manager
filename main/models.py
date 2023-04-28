from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 使用者資訊
class UserInfo(models.Model):
    # 身分
    UserData = models.OneToOneField(User, verbose_name='身分', on_delete=models.CASCADE)

    #使用者類別
    USERTYPES = [
        (0, '管理員'),
        (1, '老師'),
        (2, '學生')
    ]

    UserType = models.IntegerField('使用者類別', choices=USERTYPES)

    # 姓名
    Name = models.CharField('姓名', max_length=75)

    # 學號
    Id = models.IntegerField('學號')

    # Email
    Email = models.EmailField('Email', blank=True, null=True)

    # 年級
    GRADES = [
        (0, '無'),
        (7, '七年級'),
        (8, '八年級'),
        (9, '九年級'),
        (1, '高一'),
        (2, '高二'),
        (3, '高三')
    ]

    Grade = models.IntegerField('年級', choices=GRADES)

    # 班級
    Class = models.IntegerField('班級')

    # 座號
    SearNumber = models.IntegerField('座號')

    # 備註
    Note = models.TextField('備註', blank=True, null=True)

# 載具
class Device(models.Model):
    # 載具名稱
    Name = models.CharField('載具名稱')

    # 載具從屬人
    Owner = models.ForeignKey(User, verbose_name="擁有人", on_delete=models.CASCADE)

    # 載具卡號
    Id = models.CharField('載具卡號')

    # 備註
    Note = models.TextField('備註', blank=True, null=True)

# 群組
class Group(models.Model):
    # 群組名稱
    Name = models.CharField('群組名稱')

    # 身分
    UserData = models.ManyToManyField(UserInfo, verbose_name="身分")

    # 備註
    Note = models.TextField('備註', blank=True, null=True)