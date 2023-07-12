from os import name
from django.urls import path
from . import views
import asignaturas


urlpatterns = [
    path('', views.inicio, name='login'),
    path('success', views.logear_usuario, name='logear'),
    path('asignaturas', views.asignaturas, name='asignaturas'),
    path('asignaturas/crear', views.crear_asignatura, name='crear_asignatura'),
    path('asignaturas/editar/<int:id>' ,views.editar_asignatura, name='editar_asignatura'),
    path('asignaturas/eliminar/<int:id>', views.eliminar_asignatura, name ='eliminar_asignatura'),
    path('asignaturas/filtrar/', views.filtrar_asignatura, name='filtrar_asignatura'),
    
]