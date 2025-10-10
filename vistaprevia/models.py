from django.db import models

# Create your models here.
class Producto(models.Model):
    producto = models.CharField(max_length= 200)
    fecha_de_publicacion = models.DateTimeField('Fecha de publicacion')
    #este metodo str nos permite mostrar el nombre que le ponemos en el sitio admin de la pagina web
    def __str__(self, ):
        return self.producto + "---" + str(self.fecha_de_publicacion)

#aca ponemos los ORM en principio, mas adelante vamos a tener nuestros propios mdoelos en una zona aparte