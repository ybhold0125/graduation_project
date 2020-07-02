from rest_framework import serializers
from .models import News, SwipePicture, Announcement


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class SwipePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwipePicture
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
