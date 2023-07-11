from turtle import title
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Asignaturas, Usuarios
from .forms import AsignaturaForm
# Create your views here.

def inicio(request):
    return HttpResponse("<h1> Bienvenido </h1>")

def asignaturas(request):
    asignaturas = Asignaturas.objects.all()
    return render(request, 'vistas_asignaturas/asignaturas.html', {'asignaturas': asignaturas})

def crear_asignatura(request):
    formulario = AsignaturaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('asignaturas')
    return render(request, 'vistas_asignaturas/crear_asignatura.html', {'formulario': formulario})

def editar_asignatura(request, id):
    asignatura = Asignaturas.objects.get(id=id)
    formulario = AsignaturaForm(request.POST or None, instance = asignatura)
    return render(request, 'vistas_asignaturas/editar_asignatura.html', {'formulario': formulario})

def eliminar_asignatura(request, id):
    asignatura = Asignaturas.objects.get(id=id)
    asignatura.delete()
    return redirect('asignaturas')

def filtrar_asignatura(request):
    query = request.GET.get('filtrar')
    if query:
        asignaturas = Asignaturas.objects.filter(nombre__contains=query)
        return render(request, 'vistas_asignaturas/asignaturas.html', {'asignaturas': asignaturas})
    else:
        asignaturas = Asignaturas.objects.all()
        return render(request, 'vistas_asignaturas/asignaturas.html', {'asignaturas': asignaturas})