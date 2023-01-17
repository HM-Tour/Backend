from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers  import PostSerializer

from .models import Post


class PostListView(ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class= PostSerializer
    

class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class= PostSerializer

class GetImagesView(APIView):
    def get(self, request, format=None):
        if Post.objects.all().exists():
            images = Post.objects.all()
            images = PostSerializer(images, many=True)

            return Response(
                {'images': images.data},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'error': 'No images found'},
                status=status.HTTP_404_NOT_FOUND
            )


class ImageUploadView(APIView):
    def post(self, request):
        try:
            data = self.request.data

            image = data['image']
            alt_text = data['alt_text']
            Title = data['Title']
            Description = data['Description']
            Date = data['Date']
            Rate = data['Rate']
            Location = data['Location']
            Cost = data['Cost']

            Post.objects.create(
                image=image,
                alt=alt_text,
                Title=Title,
                Description=Description,
                Date=Date,
                Rate=Rate,
                Location=Location,
                Cost=Cost,
            )

            return Response(
                {'success': 'Successfully uploaded image'},
                status=status.HTTP_201_CREATED
            )
        except:
            return Response(
                {'error': 'Something went wrong when uploading image'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )