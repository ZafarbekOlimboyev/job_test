from rest_framework.serializers import ModelSerializer

from .models import ConferenceDaysModel, ConferenceAgendaModel, SponsorPartnersModel


class ConferenceDaysSerializer(ModelSerializer):
    class Meta:
        model = ConferenceDaysModel
        fields = '__all__'


class ConferenceAgendaSerializer(ModelSerializer):
    class Meta:
        model = ConferenceAgendaModel
        fields = '__all__'


class SponsorPartnerSerializer(ModelSerializer):
    class Meta:
        model = SponsorPartnersModel
        fields = '__all__'
