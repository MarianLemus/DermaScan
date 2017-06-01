from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
#from django.contrib.auth.models import User
from .models import Doctor_info
from .serializers import DoctorInfoSerializer

class InfoDoctor(generics.ListCreateAPIView):
#    def get(self, request):
        queryset = Doctor_info.objects.all()
        serializer_class = DoctorInfoSerializer#(pacientes, many=True)
        #print(serializer.data)
        #return Response(serializer.data,status=status.HTTP_200_OK)
