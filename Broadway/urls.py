from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# URL Patterns to redirect to different apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('u/', include('user.urls')),
] 
