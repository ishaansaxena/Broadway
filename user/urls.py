from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    url(
        r'^login/$',
        auth_views.login,
        name = 'login',
        kwargs = {
            'template_name': 'user/login.html',
            'authentication_form': LoginForm,
        }
    ),
    url(
        r'^logout/$',
        auth_views.logout,
        name = 'logout',
        kwargs = {
            'next_page': '/'
        }
    ),
]
