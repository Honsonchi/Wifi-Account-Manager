from django.shortcuts import render
from django.views.generic import ListView
from .models import Device

# Create your views here.

# 裝置管理
class DeviceManaging(ListView):
    model = Device

    context_object_name = 'devices'

    template_name = 'device_managing.html'