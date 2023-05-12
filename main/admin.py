from django.contrib import admin
from .models import UserInfo, Device, Group

# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Device)
admin.site.register(Group)