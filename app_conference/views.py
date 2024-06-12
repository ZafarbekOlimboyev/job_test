from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser

from config.permissions import IsAdminOrReadOnly
from .models import SponsorPartnersModel, ConferenceAgendaModel, ConferenceDaysModel
from .Serializers import ConferenceDaysSerializer, ConferenceAgendaSerializer, SponsorPartnerSerializer, \
    ConferenceAgendaGetSerializer


class ConferenceDaysViewSet(ModelViewSet):
    queryset = ConferenceDaysModel.objects.all()
    serializer_class = ConferenceDaysSerializer
    permission_classes = [IsAdminOrReadOnly, ]


class ConferenceAgendaViewSet(ModelViewSet):
    queryset = ConferenceAgendaModel.objects.all()
    permission_classes = [IsAdminOrReadOnly, ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ConferenceAgendaGetSerializer
        return ConferenceAgendaSerializer


class SponsorPartnerViewSet(ModelViewSet):
    queryset = SponsorPartnersModel.objects.all()
    serializer_class = SponsorPartnerSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    parser_classes = (MultiPartParser, FormParser)
