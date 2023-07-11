from django.contrib import admin
from .models import Asignaturas
from .models import Usuarios
# Register your models here.

admin.site.register(Asignaturas)
admin.site.register(Usuarios)