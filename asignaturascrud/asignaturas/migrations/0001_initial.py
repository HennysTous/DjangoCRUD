# Generated by Django 3.2 on 2023-07-11 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignaturas',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('nombrecompleto', models.CharField(db_column='nombreCompleto', max_length=20)),
                ('descripcion', models.CharField(max_length=40)),
                ('areaconocimiento', models.CharField(db_column='areaConocimiento', max_length=20)),
                ('carrera', models.CharField(max_length=20)),
                ('creditos', models.IntegerField()),
                ('contenidotematico', models.CharField(db_column='contenidoTematico', max_length=40)),
                ('semestre', models.IntegerField()),
                ('profesor', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'asignaturas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('cc', models.IntegerField(primary_key=True, serialize=False)),
                ('pass_field', models.CharField(db_column='pass', max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('genero', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('respuesta', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'usuarios',
                'managed': False,
            },
        ),
    ]
