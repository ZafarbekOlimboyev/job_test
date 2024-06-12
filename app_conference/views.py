from rest_framework.viewsets import ModelViewSet

from config.permissions import IsAdminOrReadOnly
from .models import SponsorPartnersModel, ConferenceAgendaModel, ConferenceDaysModel
from .Serializers import ConferenceDaysSerializer, ConferenceAgendaSerializer, SponsorPartnerSerializer


class ConferenceDaysViewSet(ModelViewSet):
    queryset = ConferenceDaysModel.objects.all()
    serializer_class = ConferenceDaysSerializer
    permission_classes = [IsAdminOrReadOnly, ]


class ConferenceAgendaViewSet(ModelViewSet):
    queryset = ConferenceAgendaModel.objects.all()
    serializer_class = ConferenceAgendaSerializer
    permission_classes = [IsAdminOrReadOnly, ]


class SponsorPartnerViewSet(ModelViewSet):
    queryset = SponsorPartnersModel.objects.all()
    serializer_class = SponsorPartnerSerializer
    permission_classes = [IsAdminOrReadOnly, ]
