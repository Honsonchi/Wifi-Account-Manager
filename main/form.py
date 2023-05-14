from django import forms
from .models import Device
import re

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('Name', 'Owner', 'MacAddress', 'Note')

    def clean_MacAddress(self, *args, **kwargs):
        mac_address = self.cleaned_data.get('MacAddress')

        pattern = re.compile(r'[0-9a-fA-F]{12}')

        if not pattern.match(mac_address):
            raise forms.ValidationError('Mac位址格式有誤')

        return mac_address
    
    def clean(self):
        self.cleaned_data['MacAddress'] = self.cleaned_data['MacAddress'].upper()