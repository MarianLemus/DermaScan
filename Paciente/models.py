from django.db import models
from django.contrib.auth.models import User
from Doctor.models import Doctor_info
import datetime

class Expediente(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField('date', default=datetime.date.today())
    nacionalidad = models.CharField(max_length=50)
    sexo = models.CharField(choices=(('M','Mujer'),('H','Hombre')), max_length=16)
    edad = models.IntegerField()
    piel = models.CharField(choices=(('B','Blanco'),('N','Negro'),('A','Asiatico')), max_length=16)
    diagnosticado = models.CharField(choices=(('S','SI'),('N','NO')), max_length=16)
    biografia = models.TextField()
    doctor = models.ForeignKey(Doctor_info, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'{0}={1}'.format(self.paciente,self.diagnosticado)

class Images(models.Model):
    id = models.AutoField(primary_key=True)
    propietario = models.ForeignKey(User,on_delete=models.CASCADE)
    descripción = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
#    tags = ArrayField(
#        models.CharField(max_length=50),
#        null=True
#    )
    imagen = models.ImageField(upload_to="images/")
