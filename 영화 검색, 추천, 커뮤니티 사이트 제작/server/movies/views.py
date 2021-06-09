from django.shortcuts import render
from .models import Movie, Genre
import requests
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# 장르 목록 페이지 url로 요청을 보낸다.
# 받아온 요청을 json()으로 처리해서 딕셔너리로 만든다.
# 리스트 목록을 genres에 저장한다.
# Genre 객체를 생성한다.
# 불러온 리스트의 id를 idx, name을 name에 저장한다.
def get_genre():
    url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=ae01981c2d147b4cee80932ff6b6e6b5'
    res = requests.get(url)
    res = res.json()
    genres = res['genres']
    for genre in genres:
        genre_model = Genre()
        genre_model.idx = genre['id']
        genre_model.name = genre['name']
        genre_model.save()


# 복잡하게 적혀 있지만 그냥 인기있는 영화 api요청 url 생성하는 함수
def get_url(category='movie', feature='popular', **kwargs):
    key = 'ae01981c2d147b4cee80932ff6b6e6b5'
    url = 'https://api.themoviedb.org/3'
    url = f'{ url }/{ category }/{ feature }'
    url += f'?api_key={ key }'
    for k, v in kwargs.items():
        url += f'&{k}={v}'
    return url


# 요청을 보낸 후 응답을 반환한다.
def get_request(url):
    res = requests.get(url)
    res = res.json()
    return res


def add_movie(movie_item, now_playing=False):
    movie = Movie()
    if Movie.objects.filter(title=movie_item['title']).exists():
        return
    movie.title = movie_item['title']
    if movie_item.get('release_date', None) == None:
        movie.release_date = '1900-01-01'
    else:
        movie.release_date = movie_item['release_date']
    movie.vote_count = movie_item['vote_count']
    movie.vote_average = movie_item['vote_average']
    movie.overview = movie_item['overview']
    movie.poster_path = movie_item['poster_path']
    if now_playing == True:
        movie.now_playing = True
    movie.save()
    # 장르 id 목록을 받아온 후 genres에 저장한다.
    # genre_id와 같은 값을 가진 Genre 객체를 찾아 movie에 더해준다.
    genres = movie_item['genre_ids']
    for genre in genres:
        movie_genre = Genre.objects.filter(idx=genre)[0]
        movie.genres.add(movie_genre)


@api_view(['GET'])
def get_movie(request):
    raw_movie_list = [] # 불러온 영화 JSON을 저장할 리스트
    now_playing_movie_list = []
    get_genre() # Genre를 생성하는 함수

    # page 1~5까지 반복하면서 요청을 보내고 받아온 요청을 raw_movie_list에 저장한다.
    for i in range(1,6):
        res = get_request(get_url(page=i))['results']
        raw_movie_list += res
    
    res = get_request(get_url(feature='now_playing', region='KR'))['results']
    now_playing_movie_list += res

    # 저장된 영화를 하나씩 반복하면서 영화 객체를 생성한다.
    # 각각의 항목에 맞게 값을 넣어주고 movie id를 생성하기 위해 저장한다.
    for movie_item in now_playing_movie_list:
        add_movie(movie_item, True)
    for movie_item in raw_movie_list:
        add_movie(movie_item)
        
    # 데이터를 반환해주는 부분
    movie_list = Movie.objects.all()
    serializer = MovieSerializer(movie_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def print_movie(request):
    # 데이터를 반환해주는 부분
    movie_list = Movie.objects.all()
    serializer = MovieSerializer(movie_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def print_now_playing_movie(request):
    movie_list = Movie.objects.filter(now_playing=True)
    serializer = MovieSerializer(movie_list, many=True)
    return Response(serializer.data)