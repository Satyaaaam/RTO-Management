from django import template
from rtoapp.models import *
register = template.Library()

@register.filter(name="mystrip")
def mystrip(data):
    data = data[1:-1]
    return data

@register.filter(name='to_int')
def to_int(value):
    return int(value)
