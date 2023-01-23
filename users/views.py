from rest_framework import viewsets
from rest_framework import permissions, status
from .models import CustomUser
from .serializers import CustomUserSerializer,UpdateUserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication



from django.contrib.auth.hashers import make_password

from rest_framework.generics import (
    RetrieveUpdateAPIView

)

class CustomUserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = (TokenAuthentication,)

   
    
    def perform_create(self, serializer):
        password = self.request.data.get("password")
        hashed_password = make_password(password)
        serializer.save(password=hashed_password)

    
    


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:
            data = request.data

            firstName = data['firstName']
            lastName = data['lastName']
            location = data['location']
            description = data['description']
            email=data['email']
            username = data['username']
            password = data['password']
            re_password = data['re_password']

            if password == re_password:
                if len(password) >= 8:
                    if not CustomUser.objects.filter(username=username).exists():
                        hashed_password = make_password(password)
                        user = CustomUser.objects.create_user(
                            firstName=firstName,
                            lastName=lastName,
                            location=location,
                            description=description,
                            username=username,
                            email=email,
                            password=hashed_password,
                        )

                        user.save()

                        if CustomUser.objects.filter(username=username).exists():
                            return Response(
                                {'success': 'Account created successfully'},
                                status=status.HTTP_201_CREATED
                            )
                        else:
                            return Response(
                                {'error': 'Something went wrong when trying to create account'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                            )
                    else:
                        return Response(
                            {'error': 'Username already exists'},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response(
                        {'error': 'Password must be at least 8 characters in length'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {'error': 'Passwords do not match'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {'error': 'Something went wrong when trying to register account'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ProfileUpdate(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UpdateUserSerializer
    fields = ["firstName", "lastName", "location", "description"]