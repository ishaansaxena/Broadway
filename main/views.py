from django.shortcuts import render
from django.http import HttpResponse
from user.models import Profile, Follow

# Index view for broadway app. Loads main/index template
def index(request):
    user_profile = Profile.objects.get(user=request.user)
    following = Follow.objects.get(main_user=user_profile)
    context = {}
    return render(request, 'main/index.html', context)
