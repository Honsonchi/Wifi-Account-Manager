from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import inlineformset_factory
from .models import Device, User, UserInfo
import re

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('Name', 'MacAddress', 'Note')

    def clean_MacAddress(self, *args, **kwargs):
        mac_address = self.cleaned_data.get('MacAddress')
        
        pattern = re.compile(r'[0-9a-fA-F]{12}')

        if not pattern.match(mac_address):
            raise forms.ValidationError('MAC位址格式有誤')

        return mac_address.upper()
    
class AdminDeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('Owner', 'Name', 'MacAddress', 'Note')

    def clean_MacAddress(self, *args, **kwargs):
        mac_address = self.cleaned_data.get('MacAddress')
        
        pattern = re.compile(r'[0-9a-fA-F]{12}')

        if not pattern.match(mac_address):
            raise forms.ValidationError('MAC位址格式有誤')

        return mac_address.upper()
    
class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']
    
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        del self.fields['password2']

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['Name', 'UserType', 'StuId', 'Email', 'Grade', 'Class', 'SeatNumber', 'Internet']


class BaseUserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class BaseUserInfoEditForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['Name', 'UserType', 'StuId', 'Email', 'Grade', 'Class', 'SeatNumber', 'Internet']

BaseUserCreateFormSet = inlineformset_factory(parent_model=User, model=UserInfo, form=UserInfoForm, extra=1, can_delete=False)