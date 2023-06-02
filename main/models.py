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
    StuId = models.IntegerField('學號')

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
    SeatNumber = models.IntegerField('座號')

    # 備註
    Note = models.TextField('備註', blank=True, null=True)

    def __str__(self):
        if self.UserType == 0:
            return f'管理員 {self.Name}'
        elif self.UserType == 1:
            return f'教師 {self.Name}'
        else:
            return f'{self.Grade}{self.Class:02d}{self.SeatNumber:02d} {self.Name}'

# 載具
class Device(models.Model):
    # 載具名稱
    Name = models.CharField('載具名稱', max_length=100)

    # 載具從屬人
    Owner = models.ForeignKey(UserInfo, verbose_name="擁有人", on_delete=models.CASCADE)

    # MAC位址
    MacAddress = models.CharField('MAC位址', max_length=12)

    # 備註
    Note = models.TextField('備註', blank=True, null=True)

    def __str__(self):
        if self.Owner.UserType == 0:
            return f'{self.MacAddress} | 管理員 {self.Owner.Name} 的 {self.Name}'
        elif self.Owner.UserType == 1:
            return f'{self.MacAddress} | 教師 {self.Owner.Name} 的 {self.Name}'
        else:
            return f'{self.MacAddress} | {self.Owner.Grade}{self.Owner.Class:02d}{self.Owner.SeatNumber:02d} {self.Owner.Name} 的 {self.Name}'

# 群組標籤
class Tag(models.Model):
    # 標籤名稱
    Name = models.CharField('標籤名稱', max_length=100)

    # 備註
    Note = models.TextField('備註', blank=True, null=True)

    def __str__(self):
        return f'{self.Name}'

# 群組
class Group(models.Model):
    # 群組名稱
    Name = models.CharField('群組名稱', max_length=100)

    # 身分
    UserData = models.ManyToManyField(UserInfo, verbose_name="身分")

    # Tag
    Tag = models.ManyToManyField(Tag, verbose_name="標籤")

    # 備註
    Note = models.TextField('備註', blank=True, null=True)

    def __str__(self):
        return f'{self.Name}'

# 自訂權限
class PermissionSupport(models.Model):
    class Meta():
        managed = False # 不會再Database中創建表
        default_permissions = () # 刪除預設權限
        permissions = [('admin', 'Admin can use this service'),
                       ('can_assess', 'Can assess')]