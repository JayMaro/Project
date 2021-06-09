from .models import Review, Comment
from rest_framework import fields, serializers
from accounts.serializers import UserSerializer

class ReviewSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y년-%m월-%d일 %H시%M분", required=False, read_only=True)
    updated_at = serializers.DateTimeField(format="%Y년-%m월-%d일 %H시%M분", required=False, read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', )

class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y년-%m월-%d일 %H시%M분", required=False, read_only=True)
    updated_at = serializers.DateTimeField(format="%Y년-%m월-%d일 %H시%M분", required=False, read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', )
