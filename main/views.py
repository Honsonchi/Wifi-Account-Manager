from django.urls import path, reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Device

# Create your views here.

# 裝置管理
class DeviceManaging(ListView):
    model = Device

    context_object_name = 'devices'
    template_name = 'device_managing.html'

class DeviceEdit(UpdateView):
    model = Device
    
    fields = ['Name', 'Owner', 'MacAddress', 'Note']
    
    def get_success_url(self):
        return reverse_lazy('device_managing')

    pk_url_kwarg = 'deviceid'
    context_object_name = 'device'
    template_name = 'device_edit.html'

class DeviceDelete(DeleteView):
    model = Device
    
    def get_success_url(self):
        return reverse_lazy('device_managing')

    pk_url_kwarg = 'deviceid'
    context_object_name = 'device'
    template_name = 'device_delete.html'

class DeviceCreate(CreateView):
    model = Device
    
    fields = ['Name', 'Owner', 'MacAddress', 'Note']

    def get_success_url(self):
        return reverse_lazy('device_managing')

    pk_url_kwarg = 'deviceid'
    context_object_name = 'device'
    template_name = 'device_create.html'