from django.urls import path, reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import UserInfo, Device
from .form import DeviceForm

# 首頁
class HomePage(ListView):
    model=Device

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['now_user'] = UserInfo.objects.get(UserData=self.request.user)
        else:
            context['now_user'] = ''
        return context
    
    template_name = 'homepage.html'

# 變更密碼
class PasswordChange(PasswordChangeView):
    login_url = reverse_lazy('login')

    template_name = 'registration/password.html'

# 裝置管理
class DeviceManaging(ListView):
    model = Device

    context_object_name = 'devices'
    template_name = 'device_managing.html'

# 裝置編輯
class DeviceEdit(UpdateView):
    model = Device
    form_class = DeviceForm
    
    def get_success_url(self):
        return reverse_lazy('device_managing')

    pk_url_kwarg = 'deviceid'
    context_object_name = 'device'
    template_name = 'device_edit.html'

# 裝置刪除
class DeviceDelete(DeleteView):
    model = Device
    
    def get_success_url(self):
        return reverse_lazy('device_managing')

    pk_url_kwarg = 'deviceid'
    context_object_name = 'device'
    template_name = 'device_delete.html'

# 裝置創建
class DeviceCreate(CreateView):
    model = Device
    form_class = DeviceForm

    def get_success_url(self):
        return reverse_lazy('device_managing')

    pk_url_kwarg = 'deviceid'
    context_object_name = 'device'
    template_name = 'device_create.html'