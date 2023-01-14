from django.db import models
from post.models import Post
from django.contrib.auth import get_user_model

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.body