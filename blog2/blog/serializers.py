from rest_framework import serializers
from models import Post, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.Field(source='author.username')
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'pub_date', 'tag', 'author')