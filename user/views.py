from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

# Require login to see own profile
@login_required
def profile(request):
    context = {}
    template = loader.get_template('user/profile.html')
    return HttpResponse(template.render(context, request))
