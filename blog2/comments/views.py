from rest_framework import generics, permissions
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import *


from .serializers import CommentSerializer
from .models import Comment


class CommentList(generics.ListCreateAPIView):
    model = Comment
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny,)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Comment
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny,)
