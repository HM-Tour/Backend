from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','username', 'first_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}