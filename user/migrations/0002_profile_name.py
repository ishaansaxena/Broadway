# Generated by Django 2.0.4 on 2018-04-13 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.TextField(blank=True, max_length=32),
        ),
    ]
