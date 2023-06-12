from django import template

register = template.Library()

@register.filter
def get_userdata(group, userdata):
    try:
        return group.get(UserData=userdata).Name
    
    except group.DoesNotExist:
        return ""

    