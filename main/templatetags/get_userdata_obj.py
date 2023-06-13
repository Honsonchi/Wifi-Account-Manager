from django import template

register = template.Library()

@register.filter
def get_userdata_obj(group, userdata):
    try:
        return group.get(UserData=userdata).id
    
    except:
        return group.all()[0].id

    