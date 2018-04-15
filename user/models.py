from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import main.models

# User profile model
class Profile(models.Model):
    # Profile has a user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Profile has a bio
    bio = models.TextField(max_length=512, blank=True)
    # Profile has a birth_date
    birth_date = models.DateField(null=True, blank=True)
    # Profile has a name
    name = models.CharField(max_length=32, blank=True)
    # Profile has a image
    profile_picture = models.ImageField(
        upload_to='static/assets/user_images/',
        default='static/assets/user_images/default.png',
        blank=True
    )
    # User can follow or be followed by other users
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name="followed_by"
    )
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name="follows"
    )

    # author = Author.objects.get(id=1)
    # books = author.book_set.all()

    # Return username as object descriptor
    def __str__(self):
        return self.user.username


# On save, a profile will be created
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(user=instance)

# Make the create_profile method a reciever for User saves
post_save.connect(create_profile, User)

# Activity model
class AbstractActivity(models.Model):
    activityType = models.CharField(max_length=50)
    activity_user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="activity_user",
        null=True
    )
    # class Meta:
    #     abstract = True

class AddMovieActivity(AbstractActivity):
    movie = models.OneToOneField(
        main.models.Movie,
        on_delete=models.CASCADE,
        related_name="movie"
    )

class AddUserActivity(AbstractActivity):
    user = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        related_name="related_user"
    )

