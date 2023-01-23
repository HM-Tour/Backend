from rest_framework import viewsets
from rest_framework import permissions, status
from .models import CustomUser
from .serializers import CustomUserSerializer,UserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication



class CustomUserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = (TokenAuthentication,)

   
    


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )
  

    def post(self, request):
        try:
            data = request.data

            firstName = data['firstName']
            lastName = data['lastName']
            email=data['email']
            username = data['username']
            password = data['password']
            re_password = data['re_password']

            if password == re_password:
                if len(password) >= 8:
                    if not CustomUser.objects.filter(username=username).exists():
                        user = CustomUser.objects.create_user(
                            firstName=firstName,
                            lastName=lastName,
                            username=username,
                            email=email,
                            password=password,
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


  