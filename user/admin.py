from django.contrib import admin
from .models import Profile, AbstractActivity, AddUserActivity, AddMovieActivity

# Register the Profile model for admin access
admin.site.register(Profile)
admin.site.register(AbstractActivity)
admin.site.register(AddUserActivity)
admin.site.register(AddMovieActivity)
