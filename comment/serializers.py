from rest_framework import serializers
from .models import Comment
from post.models import Post
class CommentSerializer(serializers.ModelSerializer):

    owner_username = serializers.CharField(source='owner.username', read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'post', 'owner', 'owner_username', 'body', 'created_at')
        read_only_fields = ('created_at',)

