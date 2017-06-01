from django.contrib import admin
from Doctor.models import Doctor_info

# Register your models here.
class Doctor_infoAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellidos','especialidad')
    #exclude = ('médico',)

    #def save_model(self,request,obj,form,change):
    #    obj.médico = request.user
    #    obj.save()

admin.site.register(Doctor_info, Doctor_infoAdmin)
