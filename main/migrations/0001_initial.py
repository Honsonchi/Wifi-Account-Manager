# Generated by Django 3.2.18 on 2023-05-12 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserType', models.IntegerField(choices=[(0, '管理員'), (1, '老師'), (2, '學生')], verbose_name='使用者類別')),
                ('Name', models.CharField(max_length=75, verbose_name='姓名')),
                ('StuId', models.IntegerField(verbose_name='學號')),
                ('Email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('Grade', models.IntegerField(choices=[(0, '無'), (7, '七年級'), (8, '八年級'), (9, '九年級'), (1, '高一'), (2, '高二'), (3, '高三')], verbose_name='年級')),
                ('Class', models.IntegerField(verbose_name='班級')),
                ('SeatNumber', models.IntegerField(verbose_name='座號')),
                ('Note', models.TextField(blank=True, null=True, verbose_name='備註')),
                ('UserData', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='身分')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='群組名稱')),
                ('Note', models.TextField(blank=True, null=True, verbose_name='備註')),
                ('UserData', models.ManyToManyField(to='main.UserInfo', verbose_name='身分')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='載具名稱')),
                ('MacAddress', models.CharField(max_length=12, verbose_name='MAC位址')),
                ('Note', models.TextField(blank=True, null=True, verbose_name='備註')),
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.userinfo', verbose_name='擁有人')),
            ],
        ),
    ]
