from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
#from django.contrib.auth.models import User
from .models import Expediente, Images
from .serializers import ExpedienteSerializer,ImagesSerializer

class InfoPaciente(generics.ListCreateAPIView):
#    def get(self, request):
        queryset = Expediente.objects.all()
        serializer_class = ExpedienteSerializer#(pacientes, many=True)
        #print(serializer.data)
        #return Response(serializer.data,status=status.HTTP_200_OK)
class ImagesPaciente(generics.ListCreateAPIView):
#    def get(self, request):
        queryset = Images.objects.all()
        serializer_class = ImagesSerializer#(pacientes, many=True)
