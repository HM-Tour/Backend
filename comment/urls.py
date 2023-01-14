from django.urls import path
from .views import *
urlpatterns = [
    path('post/<int:post_id>',CommentListView.as_view(), name='comments'),
    path('<int:pk>', CommentDetailView.as_view(),name='comment')
]