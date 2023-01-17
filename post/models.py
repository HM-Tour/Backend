from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Post(models.Model):

    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True, blank=True)
    Title=models.CharField(max_length=255)
    Description=models.TextField(blank=True)
    Date=models.DateTimeField(auto_now_add=True)
    Rate=models.IntegerField(default=5)
    image=models.ImageField(null=True, blank=True ,upload_to='images/')
    Location=models.TextField()
    Cost=models.FloatField()
    alt = models.CharField(null=True, blank=True,max_length=255)
# python -m pip install Pillow  -> run this command to accept the image

    def __str__(self):
        return self.Title

    class Meta:
        ordering = ["-pk"]

    @property
    def imageURL(self):

        try:
            url = self.image.url
        except:
            url = 'https://www.travel-intel.com/wp-content/uploads/2022/05/Tourism-takes-off-summer-2022.jpg'
            
        return url
 