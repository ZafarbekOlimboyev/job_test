from rest_framework.viewsets import ModelViewSet

from config.permissions import IsAdminOrReadOnly
from .models import AboutModel
from .serializes import AboutSerializer


class AboutViewSet(ModelViewSet):
    queryset = AboutModel.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [IsAdminOrReadOnly, ]
