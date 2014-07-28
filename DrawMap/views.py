from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

# Create your views here.
def index(request):
    template = loader.get_template("map.html")
    c = Context()
    return HttpResponse(template.render(c))