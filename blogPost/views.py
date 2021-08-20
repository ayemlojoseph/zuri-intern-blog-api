from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PostSerializer
from .models import  Post
from rest_framework import permissions


#Post View
class PostListAPIView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.AllowAny,) 
    def perform_create(self, serializer):
        return serializer.save()
    def get_queryset(self):
        return self.queryset.filter()

class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Post.objects.all()
    lookup_field = "id"
    def get_queryset(self):
        return self.queryset.filter()
    
