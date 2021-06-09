from django.contrib import admin

# Register your models here.
from .models import Movie, Genre
from accounts.models import User, LikeMovie
from freeboard.models import Review, Comment

admin.site.register(Movie)
admin.site.register(User)
admin.site.register(LikeMovie)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Comment)
