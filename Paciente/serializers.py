from .models import Expediente, Images
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")


class ExpedienteSerializer(serializers.ModelSerializer):
    pacientes = UserSerializer(read_only=True)
    class Meta:
        model = Expediente
        fields = ("__all__")

class ImagesSerializer(serializers.ModelSerializer):
    pacientes = UserSerializer(read_only=True)
    class Meta:
        model = Images
        fields = ("__all__")
