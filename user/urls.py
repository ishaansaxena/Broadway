from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views

urlpatterns = [
    # Default path in /u/ is profile description/editing
    path('', views.profile, name='profile'),
    # u/login is the default login path; calls the login form
    url(
        r'^login/$',
        auth_views.login,
        name = 'login',
        kwargs = {
            'template_name': 'user/login.html',
            'authentication_form': LoginForm,
        }
    ),
    # u/logout is the default logout path; gives logout command
    url(
        r'^logout/$',
        auth_views.logout,
        name = 'logout',
        kwargs = {
            'next_page': '/'
        }
    ),
    url(r'^register/$', views.register, name='register'),
    # TODO: Create path to view other profiles
]
