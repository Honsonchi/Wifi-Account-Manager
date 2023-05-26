from typing import Any, Dict
from django import forms
from .models import Device
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