from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    
 
    owner_username = serializers.CharField(source='owner.username', read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'owner', 'title','description','date', 'rate','image','location','owner_username', 'price')
      

        