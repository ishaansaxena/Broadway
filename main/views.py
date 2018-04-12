from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Index view for broadway app. Loads main/index template
def index(request):
    context = {}
    template = loader.get_template('main/index.html')
    return HttpResponse(template.render(context, request))
