from django import template
from django.template.defaultfilters import register
from rango.models import Category

@register.inclusion_tag('rango/categories.html')
def get_catgory_list(current_catrgory=None):
    return {'categories':Category.objects.all(),
            'current_category':current_catrgory}