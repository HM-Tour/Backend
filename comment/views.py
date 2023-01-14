from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers  import CommentSerializer

from .models import Comment


class CommentListView(ListCreateAPIView):
    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        queryset = Comment.objects.filter(post_id=post_id)
        return queryset
    serializer_class= CommentSerializer
    



class CommentDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class= CommentSerializer
