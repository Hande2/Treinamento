from django import template

register = template.Library()



@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()

#@register.filters(name='meu_filter')
def my_filter(data):
    return data + ' - ' + 'Alterado pelo filter'

@register.filter(name='arredonde')
def arredonda(value, casas):
    return round(value,casas)