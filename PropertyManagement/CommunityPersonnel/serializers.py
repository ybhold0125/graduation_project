from rest_framework import serializers
from .models import User
from InformationModule.models import RepairInfo, CostInfo, FeedbackInfo


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


class UserSerializer(serializers.ModelSerializer):
    repairInfo = RepairInfoSerializer(many=True)
    costInfo = CostInfoSerializer(many=True)
    feedbackInfo = FeedbackInfoSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'