from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Movie
from django.core.exceptions import ObjectDoesNotExist
from Broadway import settings
# import tmdb3

# tmdb3.set_key(settings.API_KEY)
from user.models import Profile, Follow, Activity

# Index view for broadway app. Loads main/index template
def index(request):
    user_profile = Profile.objects.get(user=request.user)
    all_activities = Activity.objects.all().order_by('-created_at')
    following = Follow.objects.filter(main_user=user_profile)
    activities = []
    for follow_relation in following:
        activities_sub = all_activities.filter(main_user=follow_relation.followed_user)
        activities.extend(list(activities_sub))
    # everyone = User.objects.filter(is_active=True)
    # active_not_deleted = list(filter(lambda user: user.is_deleted is False), list(everyone))
    # active_is_deleted = list(filter(lambda user: user.is_deleted is True), list(everyone))
    context = {
        'profile': user_profile,
        'activities': activities,
    }
    return render(request, 'main/index.html', context)
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
