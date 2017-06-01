from django.db import models
from django.contrib.auth.models import User
import datetime

class Doctor_info(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    sexo = models.CharField(choices=(('M','Mujer'),('H','Hombre')), max_length=16)
    edad = models.IntegerField()
    cédula_profesional = models.CharField(max_length=50)
    especialidad = models.CharField(choices=(('OM','Oncología Médica'),('OR','Oncología Radioterápica'),('D','Dermatología'), ('N','Nutrición'), ('P','Psicología')), max_length=16)
    experiencia = models.TextField()
    #pacientes = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'{0}={1}'.format(self.médico,self.especialidad)

    def __str__(self):
        return str(self.nombre)
