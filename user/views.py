from django.template import loader
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import RegistrationForm, ProfileUpdateForm
from .models import *
from Broadway import settings
from main.models import Movie
import tmdb3


# import pyrebase

# config = {
#     'apiKey': "AIzaSyACq-nKe1xQcY4MhhPdmRfAbiyO7-qAoP4",
#     'authDomain': "broadway-8c7ee.firebaseapp.com",
#     'databaseURL': "https://broadway-8c7ee.firebaseio.com",
#     'projectId': "broadway-8c7ee",
#     'storageBucket': "broadway-8c7ee.appspot.com",
#     'messagingSenderId': "530646122241"
# }
#Intialize Firebase
# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
# ref = firebase.database()
# Require login to see own profile
tmdb3.set_key(settings.API_KEY)

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
    # Get visited user
    user = get_object_or_404(User, username=username)
    user_profile = Profile.objects.get(user=user)
    # Get request user
    current_user = Profile.objects.get(user=request.user)
    # Check if request u follows visited u
    is_followed = False
    for follower in current_user.follow_set.all():
        if follower.followed_user == user_profile:
            is_followed = True
    context = {
        'profile': user_profile,
        'user': user,
        'is_followed': is_followed,
    }
    return render(request, 'user/peerprofile.html', context)

@csrf_exempt
def follow(request, username):
    if username == request.user.username:
        return redirect('profile')
    if request.method == "POST":
        # Get user profiles of followers and followees
        user_follower = get_object_or_404(User, username=request.user.username)
        user_to_follow = get_object_or_404(User, username=username)
        # Update follwers and following lists of users profiles
        user_profile_follower = Profile.objects.get(user=user_follower)
        user_profile_to_follow = Profile.objects.get(user=user_to_follow)
        # Check if request u follows visited u
        is_followed = False
        for follower in user_profile_follower.follow_set.all():
            if follower.followed_user == user_profile_to_follow:
                is_followed = True
        # If already followed, do nothing
        if is_followed:
            return HttpResponse("OK")
        # Create new follow relation
        follow_relation = Follow(
            main_user=user_profile_follower,
            followed_user=user_profile_to_follow
        )
        follow_relation.save()
        return HttpResponse("OK")

@csrf_exempt
def unfollow(request, username):
    if username == request.user.username:
        return redirect('profile')
    if request.method == "POST":
        user_follower = get_object_or_404(User, username=request.user.username)
        user_to_unfollow = get_object_or_404(User, username=username)

        user_profile_follower = Profile.objects.get(user=user_follower)
        user_profile_to_unfollow = Profile.objects.get(user=user_to_unfollow)
        is_following = False
        for follower in user_profile_follower.follow_set.all():
            if follower.followed_user == user_profile_to_unfollow:
                is_following = True
        if is_following:
            # Delete follow relation i.e. unfollow
            follow_relation = Follow.objects.get(
                main_user=user_profile_follower,
                followed_user=user_profile_to_unfollow
            )
            follow_relation.delete()
            return HttpResponse("OK")
        else:
            #If not following do nothing
            return HttpResponse("OK")


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
            # ref.child("Users").child(new_user.username).child("Name").set("Blah")
            login(request, new_user)
            return redirect('index')
    return render(request, 'user/register.html', {'form': form})

def searchMovie(request, movieId):
    try:
        movie = Movie.objects.get(movie_id=movieId)
    except ObjectDoesNotExist:
        res = tmdb3.Movie(movieId)
        movie = Movie(movie_id=movieId, title=res.title, overview=res.overview, release_date=res.releasedate,
                      rating=res.userrating, poster=res.poster, genre=res.genres)
        movie.save()

    context = {'movie' : movie}
    return render(request, "main/movie.html", context)