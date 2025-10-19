from django.db import models

# Create your models here.
class Datosusuarios(models.mODEL):

    usuario =models.ForeignKey(User, blanck = False, null = True, on_delete= models.CASCADE)