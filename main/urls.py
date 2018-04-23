from django.urls import path
from django.conf.urls import url
from . import views
from user import views as userviews
# Index for the Broadway App
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^q/(?P<query>[\w\-&]+)/$', views.search, name='search'),
    url(r'^m/(?P<ids>[0-9]+)/$', views.moviedetails, name='moviedetails'),
    url(r'^m/(?P<movieId>[0-9]+)/add$', userviews.add_watchlist, name='user_add_watchlist'),
    url(r'^m/(?P<movieId>[0-9]+)/remove$', userviews.remove_watchlist, name='user_remove_watchlist'),
    
]