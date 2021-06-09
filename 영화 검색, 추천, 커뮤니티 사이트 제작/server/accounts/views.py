from random import random
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, LikeMovieSerializer
from .models import LikeMovie

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from movies.models import Movie
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from django_seed import Seed
import random


# Create your views here.
@api_view(['POST'])
def signup(request):
	#1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	#1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	#2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
        # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['POST', 'GET'])  
@authentication_classes([JSONWebTokenAuthentication])       # JWT가 유효한지 체크
@permission_classes([IsAuthenticated])          # 인증이 되어있는 상태인지 체크
def like_movie(request):
    if request.method == 'POST':
        serializer = LikeMovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if LikeMovie.objects.filter(movie_id=request.data['movie'], user_id=request.user.id).exists():
                like_movie = LikeMovie.objects.filter(movie_id=request.data['movie'], user_id=request.user.id)[0]
                if request.data['rating'] == 0:
                    like_movie.delete()
                else:
                    like_movie.rating = request.data['rating']
                    like_movie.save()
            else:
                if request.data['rating'] != 0:
                    serializer.save(user=request.user)
    else:
        like_movies = LikeMovie.objects.filter(user_id=request.user.id)
        serializer = LikeMovieSerializer(like_movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def cf_algo(request, movie_id):
    like_movie_list = LikeMovie.objects.all()
    serializer = LikeMovieSerializer(like_movie_list,many=True)
    df = pd.json_normalize(serializer.data)
    movie_user_rating = df.pivot_table('rating', index='movie', columns='user')
    movie_user_rating.fillna(0, inplace=True)
    item_based_collabor = cosine_similarity(movie_user_rating)
    item_based_collabor = pd.DataFrame(data = item_based_collabor, index=movie_user_rating.index, columns=movie_user_rating.index)
    
    df_list = item_based_collabor[movie_id].sort_values(ascending=False)[1:7]
    df_index = list(df_list.index.values)
    return Response(df_index)


@api_view(['GET'])
def dummy_user(request):
    User = get_user_model()
    seeder = Seed.seeder()
    seeder.add_entity(User, 10)
    seeder.execute()
    return Response(status=status.HTTP_201_CREATED)
    

@api_view(['GET'])
def dummy(request):
    for _ in range(500):
        User = get_user_model()
        random_movie = Movie.objects.order_by("?")[0]
        random_user = User.objects.order_by("?").first()
        rating = random.randint(1, 5)
        Dummy = LikeMovie()
        Dummy.user = random_user
        Dummy.movie = random_movie
        Dummy.rating = rating
        if LikeMovie.objects.filter(user=random_user, movie=random_movie).exists():
            continue
        Dummy.save()
    return Response(status=status.HTTP_201_CREATED)


## 🚩admin 페이지 redirect 시켜주기
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])       # JWT가 유효한지 체크
@permission_classes([IsAuthenticated])  
def manager(request):
    if request.user.is_superuser == True:
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)

