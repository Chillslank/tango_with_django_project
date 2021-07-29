from django import template
from django.template.defaultfilters import register
from rango.models import Category

@register.inclusion_tag('rango/categories.html')
def get_catgory_list():
    return {'categories':Category.objects.all()}