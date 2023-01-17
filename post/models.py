from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Post(models.Model):

    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True, blank=True)
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    date=models.DateTimeField(auto_now_add=True)
    rate=models.IntegerField(default=5)
    image=models.ImageField(null=True, blank=True)
    location=models.TextField()
    price=models.FloatField()

# python -m pip install Pillow  -> run this command to accept the image

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-pk"]

    @property
    def imageURL(self):

        try:
            url = self.image.url
        except:
            url = 'https://www.travel-intel.com/wp-content/uploads/2022/05/Tourism-takes-off-summer-2022.jpg'
            
        return url