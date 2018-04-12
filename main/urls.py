from django.urls import path
from . import views

# Index for the Broadway App
urlpatterns = [
    path('', views.index, name='index'),
]
