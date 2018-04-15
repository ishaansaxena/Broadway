from django.db import models

import Broadway.settings as settings

import tmdb3
import user.models
# Create your models here.

class Movie(models.Model):

 import tmdb3
# Create your models here.

class Movie(models.Model):
    #movie has id in database
    id = models.IntegerField(primary_key=True)

    #title of movie
    title = models.CharField(max_length=100)
    #overview of movie
    overview = models.TextField()
    #movie release date
    release_date = models.DateField()
    #user ratings of movie
    rating = models.FloatField()
    #poster representing movie
    poster = models.ImageField()
    #genre
    genre = models.CharField(max_length=100)

    #return movie title as object descriptor
    def __str__(self):
        return self.title



class AbstractActivity(models.Model):
    activityType = models.CharField(max_length=50)

    class Meta:
        abstract = True

class AddMovieActivity(AbstractActivity):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class AddUserActivity(AbstractActivity):
    user = user.models.Profile


