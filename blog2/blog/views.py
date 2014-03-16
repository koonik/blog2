from rest_framework import generics, permissions
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import *


from .serializers import PostSerializer, TagSerializer
from .models import Post, Tag


class PostList(generics.ListCreateAPIView):
    model = Post
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)

    def pre_save(self, obj):
        obj.author = self.request.user



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Post
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)


class TagList(generics.ListCreateAPIView):
    model = Tag
    serializer_class = TagSerializer
    permission_classes = (permissions.AllowAny,)


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Tag
    serializer_class = TagSerializer
    permission_classes = (permissions.AllowAny,)


def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
    return HttpResponseRedirect('/blog/')


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/blog/')