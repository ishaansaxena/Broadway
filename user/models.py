from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
import main.models
from main.models import Movie

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
    # User has followers and following
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    # Activities for all users can be gotten by a similar relation
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
class Activity(models.Model):
    activity_type = models.CharField(max_length=50)
    main_user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="main_user",
        null=True
    )
    movie = models.ForeignKey(
        main.models.Movie,
        on_delete=models.CASCADE,
        related_name="movie",
        null=True,
        blank=True
    )
    activity_user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="activity_user",
        null=True,
        blank=True
    )
    def __str__(self):
        return str(self.main_user) + " >> " + self.activity_type

# Follow model
class Follow(models.Model):
    main_user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True
    )
    followed_user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="followed_user"
    )

    # Return username as object descriptor
    def __str__(self):
        return str(self.main_user) + " " + str(self.followed_user)

def follow_post_save(sender, instance, created, **kwargs):
    if created:
        instance.main_user.following += 1
        instance.followed_user.followers += 1
        instance.main_user.save()
        instance.followed_user.save()
        # Create an activity
        activity = Activity(
            activity_type="followed",
            main_user=instance.main_user,
            activity_user=instance.followed_user
        )
        activity.save()

def follow_pre_delete(sender, instance, **kwargs):
    instance.main_user.following -= 1
    instance.followed_user.followers -= 1
    instance.main_user.save()
    instance.followed_user.save()
    # Delete follow activity
    activity = Activity.objects.get(
        activity_type="followed",
        main_user=instance.main_user,
        activity_user=instance.followed_user
    )
    activity.delete()

post_save.connect(follow_post_save, Follow)
pre_delete.connect(follow_pre_delete, Follow)

#module for user's
class Watchlist(models.Model):
    main_user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True
    )

    movie_watchlist_element = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="movie"
    )

