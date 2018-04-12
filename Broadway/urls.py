from django.contrib import admin
from django.urls import path, include

# URL Patterns to redirect to different apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('u/', include('user.urls')),
]
