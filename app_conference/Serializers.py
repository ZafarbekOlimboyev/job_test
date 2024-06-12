from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import ConferenceDaysModel, ConferenceAgendaModel, SponsorPartnersModel


class ConferenceDaysSerializer(ModelSerializer):
    class Meta:
        model = ConferenceDaysModel
        fields = '__all__'


class ConferenceAgendaSerializer(ModelSerializer):
    class Meta:
        model = ConferenceAgendaModel
        fields = '__all__'


class ConferenceAgendaGetSerializer(ModelSerializer):
    day_info = SerializerMethodField(method_name='get_day_info')

    class Meta:
        model = ConferenceAgendaModel
        fields = ['title', 'oclock', 'day_info']

    def get_day_info(self, obj):
        res = {
            'id': obj.day_id.id,
            'day_number': obj.day_id.day_number,
            'date': obj.day_id.date
        }
        return res


class SponsorPartnerSerializer(ModelSerializer):
    class Meta:
        model = SponsorPartnersModel
        fields = '__all__'
