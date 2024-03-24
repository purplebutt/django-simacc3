from django import template

register = template.Library()


@register.simple_tag
def developer():
    return "CM" 

@register.simple_tag
def info_companyname():
    return "SimAcc3" 