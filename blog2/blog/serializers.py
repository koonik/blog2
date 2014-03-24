from rest_framework import serializers
from models import Post, Tag
from django.contrib.auth.models import User


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.Field(source='author.username')
    tags_detail = TagSerializer(source='tag', read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'pub_date', 'tags_detail', 'tag', 'author')


class UserSerializer(serializers.ModelSerializer):

     class Meta:
        model = User
        fields = ('id', 'username')
