from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Movie
from django.core.exceptions import ObjectDoesNotExist
from Broadway import settings
import tmdb3

tmdb3.set_key(settings.API_KEY)
from user.models import Profile, Follow

# Index view for broadway app. Loads main/index template
def index(request):
    user_profile = Profile.objects.get(user=request.user)
    following = Follow.objects.get(main_user=user_profile)
    context = {}
    template = loader.get_template('main/index.html')
    return HttpResponse(template.render(context, request))


def searchMovie(request, movieId):
    try:
        movie = Movie.objects.get(movie_id=movieId)
    except ObjectDoesNotExist:
        res = tmdb3.Movie(movieId)
        movie = Movie(movie_id=movieId, title=res.title, overview=res.overview, release_date=res.releasedate,
                      rating=res.userrating, poster=res.poster, genre=res.genres)
        movie.save()

    context = {'movie': movie}
    return render(request, "main/movie.html", context)

