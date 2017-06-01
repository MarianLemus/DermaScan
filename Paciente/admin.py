from django.contrib import admin
from Paciente.models import Expediente
from Paciente.models import Images

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('paciente','diagnosticado')
    #exclude = ('paciente',)

    #def save_model(self,request,obj,form,change):
    #    obj.médico = request.user
    #    obj.save()
class ImagesAdmin(admin.ModelAdmin):
    list_display =('propietario',)
    exclude = ('propietario',)

    def save_model(self,request,obj,form,change):
        obj.propietario = request.user
        obj.save()


admin.site.register(Expediente, PacienteAdmin)
admin.site.register(Images, ImagesAdmin)
