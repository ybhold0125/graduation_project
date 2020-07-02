from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import UserViewSet


user_info = UserViewSet.as_view({
    'get':'user_self',
    'post':'user_login',
})

urlpatterns = format_suffix_patterns([
    path('user_info/', user_info, name='user_info'),
])