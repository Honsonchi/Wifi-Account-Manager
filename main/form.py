from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from .models import Device, User, UserInfo, Group
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
    def get_choices():
        choices=[]
        for i in Group.objects.all():
            choices.append((i.id, i.Name))
        return choices

    user_group = forms.ChoiceField(widget=forms.Select, choices=get_choices(), label='所在群組')

    class Meta:
        model = UserInfo
        fields = ['Name', 'UserType', 'user_group', 'StuId', 'Email', 'Grade', 'Class', 'SeatNumber', 'Internet', 'Note']

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Excel 檔案')

BaseUserCreateFormSet = inlineformset_factory(parent_model=User, model=UserInfo, form=UserInfoForm, extra=1, can_delete=False)