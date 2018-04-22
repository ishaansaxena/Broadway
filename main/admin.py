from django.contrib import admin
from . import models
import tmdbv3api
import random

# Register your models here.
admin.site.register(models.Movie)

# add dummy movies into database
"""movie_tmdb3 = tmdbv3api.Movie()
list_movies=["Mad Max", "The Dark Knight", "Jurassic Park", "Requiem for a Dream"]
for i in range(len(list_movies)):
    tmp_movie = movie_tmdb3.search(list_movies[i])
    tmp_movie = tmp_movie[0]
    movie = models.Movie(id=tmp_movie.id, movie_id = tmp_movie.id, title=tmp_movie.title,
                         overview=tmp_movie.overview, rating=0, release_date=tmp_movie.release_date,
                         poster=tmp_movie.poster_path, genre="")

    movie.save()
"""