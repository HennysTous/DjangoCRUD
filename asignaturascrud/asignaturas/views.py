from turtle import title
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import Q
from .models import Asignaturas, Usuarios
from .forms import AsignaturaForm
import logging as L
# Create your views here.

def inicio(request):
    return render(request, 'vistas_usuario/login.html')

def logear_usuario(request):
    
    email=request.POST.get('email') 
    password=request.POST.get('pass')
    usuario = Usuarios.objects.filter(Q(email=email) & Q(pass_field=password))
    print(usuario)
    if not usuario: 
        print('Verifica que el email o la contraseña sean los correctos')
        return redirect('login')
    else:
        print('Inicio de sesion exitoso')
        return redirect('asignaturas')

def recuperar_usuario(request):
    
    email=request.GET.get('email') 
    respuesta=request.GET.get('respuesta')
    usuario = Usuarios.objects.filter(Q(email=email) & Q(respuesta=respuesta))
    print(usuario)
    if not usuario: 
        print('Verifica que el email o la contraseña sean los correctos')
        return render(request, )
    else:
        print('Inicio de sesion exitoso')
        return redirect('asignaturas')

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


