from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class TipoEntidad(models.Model):
	nombre = models.CharField(max_length=140)

class ONG(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=140)
    tipo_entidad = models.ForeignKey(TipoEntidad, on_delete=models.CASCADE)
    descripcion_breve = models.TextField(max_length=500, blank=True)
    telefono = models.CharField(max_length=20)
    sitio_web = models.CharField(max_length=140, blank=True, null=True)
    facebook = models.CharField(max_length=140, blank=True, null=True)
    logo = models.ImageField(upload_to = 'imagenes/ongs', default = 'imagenes/ongs/default.png')
    persona_responsable = models.CharField(max_length=140)
    moyor_edad = models.BooleanField()

