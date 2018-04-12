from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# User profile model
class Profile(models.Model):
    # Profile has a user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Profile has a bio
    bio = models.TextField(max_length=512, blank=True)
    # Profile has a birth_date
    birth_date = models.DateField(null=True, blank=True)
    # TODO: Add fields to Profile based on requirements

    # Return username as object descriptor
    def __str__(self):
        return self.user.username


# On save, a profile will be created
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(
            user=instance, birth_date=timezone.now
        )

# Make the create_profile method a reciever for User saves
post_save.connect(create_profile, User)
