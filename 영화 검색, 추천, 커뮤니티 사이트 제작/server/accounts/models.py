from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey, ManyToManyField

# Create your models here.
## 다른 앱의 모델을 foreignkey 로 사용하기 위해서는 'app.modelname' 형식으로 설정하면 된다.
class User(AbstractUser):
    like_movies = ManyToManyField('movies.Movie', through='LikeMovie', related_name='like_users')

class LikeMovie(models.Model):
    movie = ForeignKey('movies.Movie', on_delete=models.CASCADE)
    user = ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return self.movie



