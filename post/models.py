from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Post(models.Model):

    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    date=models.DateTimeField(auto_now_add=True)
    rate=models.IntegerField(default=5)
    image=models.URLField(blank=False)
    location=models.TextField()
    price=models.FloatField()

    def __str__(self):
        return self.title