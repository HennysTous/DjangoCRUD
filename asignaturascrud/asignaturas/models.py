# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from numpy import delete


class Asignaturas(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    nombrecompleto = models.CharField(db_column='nombreCompleto', max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(max_length=40)
    areaconocimiento = models.CharField(db_column='areaConocimiento', max_length=20)  # Field name made lowercase.
    carrera = models.CharField(max_length=20)
    creditos = models.IntegerField()
    contenidotematico = models.CharField(db_column='contenidoTematico', max_length=40)  # Field name made lowercase.
    semestre = models.IntegerField()
    profesor = models.CharField(max_length=60)

    def __str__(self) -> str:
        fila = "ID: "+ str(self.id) +"-"+"Nombre: "+self.nombre
        return fila
    
    def delete(self, using=None, keep_parents=False):
        super().delete()

    class Meta:
        managed = False
        db_table = 'asignaturas'


class Usuarios(models.Model):
    cc = models.IntegerField(primary_key=True)
    pass_field = models.CharField(db_column='pass', max_length=20)  # Field renamed because it was a Python reserved word.
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    respuesta = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        fila = "ID: "+ str(self.cc) +"-"+"Nombre: "+self.nombre
        return fila

    class Meta:
        managed = False
        db_table = 'usuarios'
