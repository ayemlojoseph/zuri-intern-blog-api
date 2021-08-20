from django.urls import path
from . import views


urlpatterns = [
    path('api/post', views.PostListAPIView.as_view(), name="Post"),
    path('api/post/<int:id>', views.PostDetailAPIView.as_view(), name="Post"),
]
