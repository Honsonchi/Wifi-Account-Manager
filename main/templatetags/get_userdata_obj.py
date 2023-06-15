from django import template

register = template.Library()

@register.filter
def get_userdata_obj(group, userdata):
    try:
        obj = group.get(UserData=userdata).id
    except:
        obj = group.all()[0].id
    return obj
    