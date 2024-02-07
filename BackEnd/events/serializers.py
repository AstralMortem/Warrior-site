from rest_framework.serializers import ModelSerializer
from .models import Competition,Attestation

class CompetitionSerializer(ModelSerializer):
    class Meta:
        model = Competition
        fields = "__all__"

class AttestationSerializer(ModelSerializer):
    class Meta:
        model = Attestation
        fields = "__all__"