from django.contrib import admin
from . import models

# Register the Profile model for admin access
admin.site.register(models.Profile)
admin.site.register(models.Follow)
admin.site.register(models.Activity)
admin.site.register(models.Watchlist)
