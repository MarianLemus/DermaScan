from django.conf.urls import url,include
from django.contrib import admin
from Paciente.views import InfoPaciente, ImagesPaciente
from Doctor.views import InfoDoctor


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^admin/info_pacientes$', InfoPaciente.as_view()),
    url(r'^admin/info_doctores$', InfoDoctor.as_view()),
    url(r'^admin/images_pacientes$', ImagesPaciente.as_view()),
    
]
