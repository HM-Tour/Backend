from django.urls import path
from .views import *
urlpatterns = [
    path('',PostListView.as_view(), name='posts'),
    path('<int:pk>', PostDetailView.as_view(),name='post'),
    path('upload', ImageUploadView.as_view()),
    path('fetch-images', GetImagesView.as_view()),
    path('user-posts/',UserPostsView.as_view(), name='user-posts'),
]