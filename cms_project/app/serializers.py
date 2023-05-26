from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Like

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, post):
        return post.like_set.count()

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'content', 'creation_date', 'owner', 'likes_count']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
