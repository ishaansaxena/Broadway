# Generated by Django 2.0.4 on 2018-04-17 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_profile_birth_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abstractactivity',
            old_name='activityType',
            new_name='activity_type',
        ),
    ]
