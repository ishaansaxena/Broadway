from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

# Require login to see own profile
@login_required
def profile(request):
    context = {}
    template = loader.get_template('user/profile.html')
    return HttpResponse(template.render(context, request))

def register(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_user = User.objects.create_user(
                email = form.cleaned_data['email'],
                username = form.cleaned_data['username']
            )
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect('index')
    return render(request, 'user/register.html', {'form': form})
