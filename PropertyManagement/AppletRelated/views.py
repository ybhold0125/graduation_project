from rest_framework import viewsets
from .serializers import AppletRelatedSerializer
from .models import AppletRelated


class AppletRelatedViewSet(viewsets.ModelViewSet):
    queryset = AppletRelated.objects.all()
    serializer_class = AppletRelatedSerializer