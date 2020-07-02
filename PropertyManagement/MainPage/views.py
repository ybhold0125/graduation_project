from rest_framework import viewsets
from .serializers import NewsSerializer, SwipePictureSerializer, AnnouncementSerializer
from .models import News, SwipePicture, Announcement


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class SwipePictureViewSet(viewsets.ModelViewSet):
    queryset = SwipePicture.objects.all()
    serializer_class = SwipePictureSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer