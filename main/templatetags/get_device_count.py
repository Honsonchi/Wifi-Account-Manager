from django import template

register = template.Library()

@register.filter
def get_device_count(device, userdata):
    return device.filter(Owner=userdata).count()