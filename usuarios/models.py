from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import time

# Create your models here.
class Datosusuarios(models.Model):

    usuario =models.ForeignKey(User, blank = False, null = True, on_delete= models.CASCADE)
    fecha_de_nacimiento = models.CharField(max_length= 50,blank = True, null= True)
    pais = models.CharField(max_length= 50, blank=True)
    provincia = models.CharField(max_length= 50, blank=True)
    ciudad = models.CharField(max_length= 50, blank=True)
    domicilio = models.CharField(max_length= 50, blank=True)
    codigo_postal = models.CharField(max_length= 50, blank=True)
    telefono = models.CharField(max_length= 50, blank=True)
    celular = models.CharField(max_length= 50, blank=True)
    documento = models.CharField(max_length= 50, blank=True)
    cuit = models.CharField(max_length= 50, blank=True)

    def __str__(self):
        return self.usuario.username


    