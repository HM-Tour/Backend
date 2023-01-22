from django.db import models
from django.contrib.auth.models import AbstractUser





class CustomUser(AbstractUser):
    firstName = models.CharField(max_length=255,null=True, blank=True)
    lastName = models.CharField(max_length=255,null=True, blank=True)
    email = models.EmailField(unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True)