from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import MessageBoardViewSet


message_list = MessageBoardViewSet.as_view({
    'get':'customize_list',
})

urlpatterns = format_suffix_patterns([
    path('message_list/', message_list, name='message_list'),
])