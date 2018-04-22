from django.urls import path
from django.conf.urls import url
from . import views

# Index for the Broadway App
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^q/(?P<query>[\w\-&]+)/$', views.search, name='search'),
    url(r'^m/(?P<ids>[0-9]+)/$', views.moviedetails, name='moviedetails')
]