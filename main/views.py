from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Movie
from django.contrib.auth.models import User
from user.models import Profile, Activity, Follow
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from user.models import Profile, Follow, Activity
from django.db.models import Q
from datetime import datetime
from tmdbv3api import Movie as m
from tmdbv3api import TV as t

# Index view for broadway app. Loads main/index template
@login_required
def index(request):
    user_profile = Profile.objects.get(user=request.user)
    all_activities = Activity.objects.all().order_by('-created_at')
    following = Follow.objects.filter(main_user=user_profile)
    activities = []
    for follow_relation in following:
        activities_sub = all_activities.filter(main_user=follow_relation.followed_user)
        activities.extend(list(activities_sub))
    movie = m()
    popular = movie.popular()[0:8]
    popular_movies = []
    for p in popular:
        movie = getmovie(p.id)
        popular_movies.append(movie)
    context = {
        'profile': user_profile,
        'activities': activities,
        'popular': popular_movies,
    }
    return render(request, 'main/index.html', context)

@csrf_exempt
def search(request, query):
    query = query.split("-")
    # movie search
    movie = m()
    m_search = movie.search(str(query))
    movies = []
    for res in m_search:
        movies.append(res)
    # tv search
    tv = t()
    t_search = tv.search(str(query))
    tv = []
    for res in t_search:
        tv.append(res)
    # user search
    users = User.objects.filter(Q(username__icontains=" ".join(query)))
    profiles = []
    for user in users:
        profiles.append(Profile.objects.get(user=user))
    context = {
        "movies": movies,
        "tv": tv,
        "profiles": profiles,
    }
    return render(request, 'main/search.html', context)

def moviedetails(request, ids):
    movie = getmovie(ids)
    context = {
        'movie': movie
    }
    return render(request,'main/movie.html', context)

def getmovie(ids):
    try:
        movie = Movie.objects.get(movie_id=ids)
    except Exception:
        movie = m()
        movie_this = movie.details(ids)
        movie_todB = Movie(
            movie_id=movie_this.id,
            title=movie_this.title,
            overview=movie_this.overview,
            release_date = datetime.strptime(movie_this.release_date, "%Y-%m-%d").date(),
            poster = movie_this.poster_path
        )
        print(movie_this.poster_path)
        movie_todB.save()
        movie = Movie.objects.get(movie_id=ids)
    return movie

#
# def searchMovie(request, movieId):
#     try:
#         movie = Movie.objects.get(movie_id=movieId)
#     except ObjectDoesNotExist:
#         res = tmdb3.Movie(movieId)
#         movie = Movie(movie_id=movieId, title=res.title, overview=res.overview, release_date=res.releasedate,
#                       rating=res.userrating, poster=res.poster, genre=res.genres)
#         movie.save()
#
#     context = {'movie': movie}
#     return render(request, "main/movie.html", context)
