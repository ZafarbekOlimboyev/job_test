from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser

from config.permissions import IsAdminOrReadOnly
from .models import (SpeakersModel, PositionsModel, UniversitiesModel,
                     CommitteeModel, CommitteeGroupModel, GenderModel)
from .serializers import (PositionSerializer, SpeakersSerializer, UniversitiesSerializer,
                          CommitteeGroupSerializer, CommitteeSerializer, GenderSerializer, CommitteeGetSerializer, )


class PositionsViewSet(ModelViewSet):
    queryset = PositionsModel.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAdminOrReadOnly, ]


class GenderViewSet(ModelViewSet):
    queryset = GenderModel.objects.all()
    serializer_class = GenderSerializer
    permission_classes = [IsAdminOrReadOnly, ]


class CommitteeGroupViewSet(ModelViewSet):
    queryset = CommitteeGroupModel.objects.all()
    serializer_class = CommitteeGroupSerializer
    permission_classes = [IsAdminOrReadOnly, ]


class UniversitiesViewSet(ModelViewSet):
    queryset = UniversitiesModel.objects.all()
    serializer_class = UniversitiesSerializer
    permission_classes = [IsAdminOrReadOnly, ]


class CommitteeViewSet(ModelViewSet):
    queryset = CommitteeModel.objects.all()
    permission_classes = [IsAdminOrReadOnly, ]
    parser_classes = (MultiPartParser, FormParser)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommitteeGetSerializer
        return CommitteeSerializer


class SpeakersViewSet(ModelViewSet):
    queryset = SpeakersModel.objects.all()
    serializer_class = SpeakersSerializer
    permission_classes = [IsAdminOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)
