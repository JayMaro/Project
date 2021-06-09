from .models import Review, Comment
from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReviewSerializer, CommentSerializer

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Create your views here.

# review 를 생성해 serializer 된 데이터만 vue로 넘긴다.
# 그러면 vue에서 해당 데이터를 review_list에 추가한다.
# request는 request.method, request.user, request.data 등 요청에 대한 여러가지 정보들이 들어있다.

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])       # JWT가 유효한지 체크
@permission_classes([IsAuthenticated])          # 인증이 되어있는 상태인지 체크

def review(request):
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)      # 유효성 검사를 통과하면 해당 모델에 바로 저장을 해주는 겁니다...
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])       # JWT가 유효한지 체크
@permission_classes([IsAuthenticated])          # 인증이 되어있는 상태인지 체크
def check_validation(request, review_pk):
    
    validation = True

    # 해당 유저만 삭제 또는 수정이 가능하도록 한다.
    if not request.user.reviews.filter(pk=review_pk).exists():
        validation = False
        return Response(validation, status=status.HTTP_403_FORBIDDEN)

    return Response(validation, status=status.HTTP_200_OK)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])       # JWT가 유효한지 체크
@permission_classes([IsAuthenticated])          # 인증이 되어있는 상태인지 체크
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    # 해당 유저만 삭제 또는 수정이 가능하도록 한다.
    if not request.user.reviews.filter(pk=review_pk).exists():
        return Response({'detail' : '권한이 없습니다'}, status=status.HTTP_403_FORBIDDEN)
    
    # 수정할 때
    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # 삭제할 때
    elif request.method == 'DELETE':
        review.delete()
        return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])       # JWT가 유효한지 체크
@permission_classes([IsAuthenticated])          # 인증이 되어있는 상태인지 체크

def comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        comment = review.comment_set.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            ## user와 review 모두 read_only 인 상태인데
            ## 두 개 모두 save 할 때 넣기 위해서 ',' 로 연결해주었습니다.
            serializer.save(user=request.user, review = review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])       # JWT가 유효한지 체크
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    # 해당 유저만 삭제 또는 수정이 가능하도록 한다.
    if not request.user.comment_set.filter(pk=comment_pk).exists():
        return Response({'detail' : '권한이 없습니다'}, status=status.HTTP_403_FORBIDDEN)
    
    # 수정할 때
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # 삭제할 때
    elif request.method == 'DELETE':
        comment.delete()
        return Response({ 'id': comment_pk }, status=status.HTTP_204_NO_CONTENT)
