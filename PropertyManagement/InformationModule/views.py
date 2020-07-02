from django.shortcuts import render
import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from rest_framework import viewsets
from .serializers import RepairInfoSerializer, CostInfoSerializer, FeedbackInfoSerializer, MessageBoardSerializer
from .models import RepairInfo, CostInfo, FeedbackInfo, MessageBoard

from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication
)
from rest_framework_simplejwt.authentication import JWTAuthentication


class RepairInfoViewSet(viewsets.ModelViewSet):
    queryset = RepairInfo.objects.all()
    serializer_class = RepairInfoSerializer

    authentication_classes = [
        SessionAuthentication,
        JWTAuthentication,
    ]

    def list(self, request, *args, **kwargs):
        queryset = RepairInfo.objects.filter(repairName=request.user)
        serialized_data = RepairInfoSerializer(queryset, many=True)
        return Response(serialized_data.data)

    def create(self, request, *args, **kwargs):
        repair_title = request.POST.get("title")
        repair_note = request.POST.get("note")
        repair_phone = request.POST.get("phone")
        RepairInfo.objects.create(
            repairName=request.user,
            repairTitle=repair_title,
            repairNote=repair_note,
            repairPhone=repair_phone
        )
        return Response('ok')


class CostInfoViewSet(viewsets.ModelViewSet):
    queryset = CostInfo.objects.all()
    serializer_class = CostInfoSerializer

    authentication_classes = [
        SessionAuthentication,
        JWTAuthentication,
    ]

    def list(self, request, *args, **kwargs):
        queryset = CostInfo.objects.filter(accountOwner=request.user)
        serialized_data = CostInfoSerializer(queryset, many=True)
        return Response(serialized_data.data)


class FeedbackInfoViewSet(viewsets.ModelViewSet):
    queryset = FeedbackInfo.objects.all()
    serializer_class = FeedbackInfoSerializer

    authentication_classes = [
        SessionAuthentication,
        JWTAuthentication,
    ]

    def list(self, request, *args, **kwargs):
        queryset = FeedbackInfo.objects.filter(feedbackName=request.user)
        serialized_data = FeedbackInfoSerializer(queryset, many=True)
        return Response(serialized_data.data)

    def create(self, request, *args, **kwargs):
        feedback_title = request.POST.get("title")
        feedback_content = request.POST.get("content")
        feedback_contact = request.POST.get("contact")
        res = FeedbackInfo.objects.create(
            feedbackName=request.user,
            feedbackTitle=feedback_title,
            feedbackContent=feedback_content,
            feedbackContact=feedback_contact,
        )
        return Response('ok')


class MessageBoardViewSet(viewsets.ModelViewSet):
    queryset = MessageBoard.objects.all()
    serializer_class = MessageBoardSerializer

    authentication_classes = [
        SessionAuthentication,
        JWTAuthentication,
    ]

    def create(self, request, *args, **kwargs):
        message_content = request.POST.get("content")
        message_nickname = request.POST.get("nickname")
        res = MessageBoard.objects.create(
            messageName=request.user,
            messageContent=message_content,
            messageNickname=message_nickname,
        )
        return Response('ok')

    def customize_list(self, request, *args, **kwargs):
        queryset = MessageBoard.objects.filter(messageName=request.user)
        serialized_data = MessageBoardSerializer(queryset, many=True)
        return Response(serialized_data.data)
