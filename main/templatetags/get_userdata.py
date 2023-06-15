from django import template

register = template.Library()

@register.filter
def get_userdata(group, userdata):
    try:
        return group.select_related().get(UserData=userdata).Name
    
    except:
        return ""

    