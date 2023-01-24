from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','username', 'email','firstName','description','lastName','location', 'password')
        extra_kwargs = {'password': {'write_only': True}}





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('firstName', 'lastName', 'username','email','password' )
        extra_kwargs = {'password': {'write_only': True}}
        
    

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('firstName', 'lastName', 'location', 'description' )
        extra_kwargs = {'password': {'write_only': True}}