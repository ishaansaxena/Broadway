from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, ProfileUpdateForm
from .models import Profile
import pyrebase

config = {
    'apiKey': "AIzaSyACq-nKe1xQcY4MhhPdmRfAbiyO7-qAoP4",
    'authDomain': "broadway-8c7ee.firebaseapp.com",
    'databaseURL': "https://broadway-8c7ee.firebaseio.com",
    'projectId': "broadway-8c7ee",
    'storageBucket': "broadway-8c7ee.appspot.com",
    'messagingSenderId': "530646122241"
}
#Intialize Firebase
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
ref = firebase.database()
# Require login to see own profile
@login_required
def profile(request):
    current_user = User.objects.get(id=request.user.id)
    user_profile = Profile.objects.get(user=current_user)
    if request.method == "POST":
        return render(request, 'user/profile.html', {})
    else:
        form = ProfileUpdateForm(instance=user_profile)
        context = {
            'form': form,
            'profile': user_profile,
        }
        return render(request, 'user/profile.html', context)

    # context = {}
    # template = loader.get_template('user/profile.html')
    # return HttpResponse(template.render(context, request))

def peer_profile(request, username):
    if username == request.user.username:
        return redirect('profile')
    user = get_object_or_404(User, username=username)
    user_profile = Profile.objects.get(user=user)
    context = {
        'profile': user_profile,
        'user': user,
    }
    return render(request, 'user/peerprofile.html', context)

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
            ref.child("Users").child(new_user.username).child("Name").set("Blah")
            login(request, new_user)

            return redirect('index')
    return render(request, 'user/register.html', {'form': form})
