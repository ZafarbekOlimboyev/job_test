from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import (UniversitiesModel, CommitteeModel, PositionsModel,
                     CommitteeGroupModel, GenderModel, SpeakersModel)


class GenderSerializer(ModelSerializer):
    class Meta:
        model = GenderModel
        fields = '__all__'


class PositionSerializer(ModelSerializer):
    class Meta:
        model = PositionsModel
        fields = '__all__'


class CommitteeGetSerializer(ModelSerializer):
    position = SerializerMethodField(method_name='get_position')
    committee_group = SerializerMethodField(method_name='get_committee_group')
    gender = SerializerMethodField(method_name='get_gender')
    university = SerializerMethodField(method_name='get_university')

    class Meta:
        model = CommitteeModel
        fields = ['id', 'name', 'image', 'position', 'committee_group', 'gender', 'university']

    def get_position(self, obj):
        return obj.position_id.position

    def get_committee_group(self, obj):
        return obj.committee_group_id.name

    def get_gender(self, obj):
        return obj.gender_id.gender

    def get_university(self, obj):
        return obj.university_id.university_name


class CommitteeGroupSerializer(ModelSerializer):
    class Meta:
        model = CommitteeGroupModel
        fields = '__all__'


class UniversitiesSerializer(ModelSerializer):
    class Meta:
        model = UniversitiesModel
        fields = '__all__'


class CommitteeSerializer(ModelSerializer):
    class Meta:
        model = CommitteeModel
        fields = '__all__'


class SpeakersSerializer(ModelSerializer):
    class Meta:
        model = SpeakersModel
        fields = '__all__'
