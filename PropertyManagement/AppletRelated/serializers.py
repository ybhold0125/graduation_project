from rest_framework import serializers
from .models import AppletRelated


class AppletRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppletRelated
        fields = '__all__'