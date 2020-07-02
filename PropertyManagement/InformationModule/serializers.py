from rest_framework import serializers
from .models import CostInfo, RepairInfo, FeedbackInfo, MessageBoard


class RepairInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairInfo
        fields = '__all__'


class CostInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostInfo
        fields = '__all__'


class FeedbackInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackInfo
        fields = '__all__'


class MessageBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageBoard
        fields = '__all__'



