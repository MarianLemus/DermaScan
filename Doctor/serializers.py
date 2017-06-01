from .models import Doctor_info
from rest_framework import serializers
#from django.contrib.auth.models import User


class DoctorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor_info
        fields = ("__all__")
