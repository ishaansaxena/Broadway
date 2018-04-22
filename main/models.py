from django.db import models

import Broadway.settings as settings

# import tmdb3
# Create your models here.

class Movie(models.Model):
    #movie has id in database
    movie_id = models.IntegerField(null=True)
    #title of movie
    title = models.CharField(max_length=100, null=True)
    #overview of movie
    overview = models.TextField(null=True)
    #movie release date
    release_date = models.DateField(null=True)
    #user ratings of movie
    rating = models.FloatField(null=True)
    #poster representing movie
    poster = models.ImageField(
        upload_to='static/assets/movies_images/',
        default='static/assets/movies_images/default.png',
        blank=True
    )

    #return movie title as object descriptor
    def __str__(self):
        return self.title
