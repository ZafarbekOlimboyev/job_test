from rest_framework.serializers import ModelSerializer

from .models import AboutModel


class AboutSerializer(ModelSerializer):
    class Meta:
        model = AboutModel
        fields = "__all__"
