from django.db import models

# Create your models here.
class Genre(models.Model):
    idx = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    now_playing = models.BooleanField(default=False)

    def __str__(self):
        return self.title
