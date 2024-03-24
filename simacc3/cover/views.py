from django.shortcuts import render
from . import data as dt

def get_homepage_content(context:dict={}):
    context['about'] = dt.about

def homepage(request):
    ctx = get_homepage_content()
    return render(request, template_name="apps/cover/homepage.html", context=ctx)