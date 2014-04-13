from django import template
from slick.models import *

register = template.Library()

@register.inclusion_tag('slick.html')
def gallery(name, *args, **kwargs):
    return {'slick': Slick.objects.get(name=name)}