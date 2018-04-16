from django.contrib import admin
from . import models

# Register the Profile model for admin access
admin.site.register(models.Profile)
admin.site.register(models.FollowRelation)
admin.site.register(models.AbstractActivity)
admin.site.register(models.AddUserActivity)
admin.site.register(models.AddMovieActivity)
