from rest_framework.test import APITestCase
from users.models import User
from .models import Video
from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

class VideoAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create_user(
            email='fan1300@naver.com',
            password='password123'
        )
    
        self.client.login(email='fan1300@naver.com', password='password123')
    
        Video.objects.create(
            title = 'test video',
            link = 'http://www.test.com',
            user = self.user
        )
    
    def test_video_list_get(self):
        # url = 'http://127.0.0.1:8000/api/v2/video'
        url = reverse('video-list')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.headers['Content-Type'], 'application/json')
        self.assertTrue(len(res.data) > 0)
        
        for video in res.data:
            self.assertIn('title', video)
    
    def test_video_list_post(self):
        url = reverse('video-list')
        
        data = {
            'title' : 'test video2',
            'link' : 'http://test.com',
            'category' : 'test category',
            'thumnail' : 'http://test.com',
            'video_file' : SimpleUploadedFile('file,mp4' b"file_content", 'video/mp4'),
            'user' : self.user.pk
        }
        
        res = self.client.post(url, data)
        
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['title'], 'test video2')
        
    def test_video_detail_get(self):
        pass
    
    def test_video_detail_put(self):
        pass
    
    def test_video_detail_delete(self):
        pass