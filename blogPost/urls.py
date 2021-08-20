from django.urls import path
from . import views


urlpatterns = [
    path('post', views.PostListAPIView.as_view(), name="Post"),
    path('post/<int:id>', views.PostDetailAPIView.as_view(), name="Post"),
]
