from django.urls import path
from . import views

# Index for the Broadway App
urlpatterns = [
    path('', views.index, name='index'),
    path('moviedetails',views.moviedetails,name='moviedetails')
]
