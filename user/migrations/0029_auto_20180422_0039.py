# Generated by Django 2.0.4 on 2018-04-22 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180422_0039'),
        ('user', '0028_auto_20180418_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
                ('movie_watchlist_element', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='main.Movie')),
            ],
        ),
        migrations.AlterField(
            model_name='activity',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='add_movie', to='main.Movie'),
        ),
    ]
