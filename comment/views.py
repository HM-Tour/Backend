from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers  import CommentSerializer

from .models import Comment
from .permissions import IsOwnerOrReadOnly

class CommentListView(ListCreateAPIView):

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        queryset = Comment.objects.filter(post_id=post_id)
        return queryset
    serializer_class= CommentSerializer
    



class CommentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset=Comment.objects.all()
    serializer_class= CommentSerializer

