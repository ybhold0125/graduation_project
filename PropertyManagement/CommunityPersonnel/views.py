from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User

from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication
)
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = [
        SessionAuthentication,
        JWTAuthentication,
    ]

    def user_self(self, request):
        queryset = User.objects.all()
        user_self = get_object_or_404(queryset, id=request.user.id)
        serializer = UserSerializer(user_self, context={'request': request})
        return Response(serializer.data)

    def user_login(self, request):
        status = {}
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_info = User.objects.filter(username=username)
        if user_info:
            user = User.objects.get(username=username)
            check_pwd = user.check_password(password)
            if check_pwd:
                status['code'] = "登录成功"
            else:
                status['code'] = "密码错误"
        else:
            status['code'] = "用户名不存在"

        return Response(status)

    # def user_update(self, request):
    #     phone = request.data["phone"]
    #     user_info = User.objects.filter(id=request.user.id)
    #     if user_info:
    #         user_info.update(
    #             phone=phone,
    #         )
    #     return Response("ok")