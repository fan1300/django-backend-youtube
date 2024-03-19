from django.shortcuts import render
from rest_framework.views import APIView
from .models import Video
from .serializers import VideoSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class VideoList(APIView):
    def get(self):
        videos = Video.objects.all()
    
        serializer = VideoSerializer(videos, many = True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        user_data = request.data
        serializer = VideoSerializer(data = user_data)
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VideoDetail():
    def get():
        pass
    
    def put():
        pass
    
    def delete():
        pass