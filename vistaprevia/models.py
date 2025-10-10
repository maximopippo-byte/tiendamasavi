from django.db import models

# Create your models here.
class Producto(models.Model):
    producto = models.CharField(max_length= 200)
    fecha_de_publicacion = models.DateTimeField('Fecha de publicacion')

#aca ponemos los ORM en principio, mas adelante vamos a tener nuestros propios mdoelos en una zona aparte