from django.contrib import admin
from .models import UserInfo, Device, Group, Tag

# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Device)
admin.site.register(Group)
admin.site.register(Tag)