from django.core.exceptions import PermissionDenied
from django.db.models.query import QuerySet
from django.urls import path, reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import UserInfo, Device, Group
from .form import DeviceForm, AdminDeviceForm

# 首頁
class HomePage(ListView):
    model=Device

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['now_user'] = UserInfo.objects.get(UserData=self.request.user)
            context['now_user_group'] = Group.objects.get(UserData__UserData=self.request.user)
        else:
            context['now_user'] = ''
            context['now_user_group'] = ''
        return context
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Device.objects.filter(Owner__UserData=self.request.user)
        return super().get_queryset()
    


    context_object_name = 'devices'
    template_name = 'homepage.html'

# 變更密碼
class PasswordChange(PermissionRequiredMixin, LoginRequiredMixin, PasswordChangeView):
    permission_required = ['main.can_assess']

    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['now_user'] = UserInfo.objects.get(UserData=self.request.user)
        else:
            context['now_user'] = ''
        return context

    template_name = 'registration/password.html'

# 裝置管理
class DeviceManaging(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Device
    permission_required = ['main.can_assess']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['now_user'] = UserInfo.objects.get(UserData=self.request.user)
        else:
            context['now_user'] = ''
        return context

    def get_queryset(self):
        return Device.objects.filter(Owner=UserInfo.objects.get(UserData=self.request.user))

    context_object_name = 'devices'
    template_name = 'device_managing.html'

# 裝置編輯
class DeviceEdit(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Device
    form_class = DeviceForm
    permission_required = ['main.can_assess']
    
    def get_success_url(self):
        return reverse_lazy('device_managing')

    def form_valid(self, form):
        now_user = UserInfo.objects.get(UserData=self.request.user)
        if not self.request.user.has_perm('main.admin'): #如果不是管理員
            if form.instance.Owner == now_user:
                return super().form_valid(form)
            else:
                raise PermissionDenied()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['now_user'] = UserInfo.objects.get(UserData=self.request.user)
        else:
            context['now_user'] = ''
        return context

    pk_url_kwarg = 'deviceid'
    context_object_name = 'device'
    template_name = 'device_edit.html'

# 裝置刪除
class DeviceDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Device
    permission_required = ['main.can_assess']
    
    def get_success_url(self):
        return reverse_lazy('device_managing')
    
    def form_valid(self, form):
        now_user = UserInfo.objects.get(UserData=self.request.user)
        if not self.request.user.has_perm('main.admin'): #如果不是管理員
            if form.instance.Owner == now_user:
                return super().form_valid(form)
            else:
                raise PermissionDenied()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['now_user'] = UserInfo.objects.get(UserData=self.request.user)
        else:
            context['now_user'] = ''
        return context

    pk_url_kwarg = 'deviceid'
    context_object_name = 'device'
    template_name = 'device_delete.html'

# 裝置創建
class DeviceCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Device
    form_class = DeviceForm
    permission_required = ['main.can_assess']

    def get_success_url(self):
        return reverse_lazy('device_managing')
    
    def form_valid(self, form):
        form.instance.Owner = UserInfo.objects.get(UserData=self.request.user)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['now_user'] = UserInfo.objects.get(UserData=self.request.user)
        else:
            context['now_user'] = ''
        return context

    pk_url_kwarg = 'deviceid'
    context_object_name = 'device'
    template_name = 'device_create.html'

#管理員: 群組管理
class GroupManaging(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Group
    permission_required = ['main.can_assess', 'main.admin']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['now_user'] = UserInfo.objects.get(UserData=self.request.user)
        else:
            context['now_user'] = ''
        return context
    
    context_object_name = 'groups'
    template_name = 'group_managing.html'

#管理員: 群組編輯
class GroupEdit(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Group
    permission_required = ['main.can_assess', 'main.admin']
    
    fields = ['Name', 'UserData', 'Tag', 'Note']

    def get_success_url(self):
        return reverse_lazy('group_managing')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['now_user'] = UserInfo.objects.get(UserData=self.request.user)
        else:
            context['now_user'] = ''
        return context

    pk_url_kwarg = 'groupid'
    context_object_name = 'group'
    template_name = 'group_edit.html'

# 管理員: 群組刪除
class GroupDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Group
    permission_required = ['main.can_assess', 'main.admin']
    
    def get_success_url(self):
        return reverse_lazy('group_managing')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['now_user'] = UserInfo.objects.get(UserData=self.request.user)
        else:
            context['now_user'] = ''
        return context

    pk_url_kwarg = 'groupid'
    context_object_name = 'group'
    template_name = 'group_delete.html'

# 裝置創建
class GroupCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Group
    permission_required = ['main.can_assess', 'main.admin']

    fields = ['Name', 'UserData', 'Tag', 'Note']

    def get_success_url(self):
        return reverse_lazy('group_managing')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['now_user'] = UserInfo.objects.get(UserData=self.request.user)
        else:
            context['now_user'] = ''
        return context

    pk_url_kwarg = 'groupid'
    context_object_name = 'group'
    template_name = 'group_create.html'

#管理員管理
class Manage(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Device
    paginate_by = 20
    permission_required = ['main.can_assess', 'main.admin']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['now_user'] = UserInfo.objects.get(UserData=self.request.user)
        else:
            context['now_user'] = ''
        return context
    
    context_object_name = 'devices'
    template_name = 'manage.html'

#管理員編輯裝置
class AdminDeviceEdit(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Device
    form_class = AdminDeviceForm
    permission_required = ['main.can_assess', 'main.admin']
    
    def get_success_url(self):
        return reverse_lazy('manage')

    def form_valid(self, form):
        now_user = UserInfo.objects.get(UserData=self.request.user)
        if not self.request.user.has_perm('main.admin'): #如果不是管理員
            if form.instance.Owner == now_user:
                return super().form_valid(form)
            else:
                raise PermissionDenied()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['now_user'] = UserInfo.objects.get(UserData=self.request.user)
        else:
            context['now_user'] = ''
        return context

    pk_url_kwarg = 'deviceid'
    context_object_name = 'device'
    template_name = 'admin_device_edit.html'

# 管理員裝置刪除
class AdminDeviceDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Device
    permission_required = ['main.can_assess', 'main.admin']
    
    def get_success_url(self):
        return reverse_lazy('manage')
    
    def form_valid(self, form):
        now_user = UserInfo.objects.get(UserData=self.request.user)
        if not self.request.user.has_perm('main.admin'): #如果不是管理員
            if form.instance.Owner == now_user:
                return super().form_valid(form)
            else:
                raise PermissionDenied()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['now_user'] = UserInfo.objects.get(UserData=self.request.user)
        else:
            context['now_user'] = ''
        return context

    pk_url_kwarg = 'deviceid'
    context_object_name = 'device'
    template_name = 'admin_device_delete.html'

# 管理員裝置新增
class AdminDeviceCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Device
    form_class = AdminDeviceForm
    permission_required = ['main.can_assess', 'main.admin']

    def get_success_url(self):
        return reverse_lazy('manage')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['now_user'] = UserInfo.objects.get(UserData=self.request.user)
        else:
            context['now_user'] = ''
        return context

    pk_url_kwarg = 'deviceid'
    context_object_name = 'device'
    template_name = 'admin_device_create.html'