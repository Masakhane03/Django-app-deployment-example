from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value,arg):
    '''
    This cuts out all values of "arg" from the string!
    '''
    return value.replace(arg,'')
# This commented line of code below is same as @register.filter(name='cut')
# register.filter('cut',cut)
