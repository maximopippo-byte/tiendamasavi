from django.db import models
from django.utils.html import format_html 

# Create your models here.

class Categoria(models.Model): 

    nombre = models.CharField(max_length=100, db_index=True) 

    slug = models.SlugField(max_length=100, db_index=True) 

 

    def __str__(self): 

        return '%s' % self.nombre 


class Producto(models.Model):
    producto = models.CharField(max_length= 200)
    fecha_de_publicacion = models.DateTimeField('Fecha de publicacion')
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", blank=True, null=True) 

    #producto, fecha de publicacion e imagen nos sirven como variables donde vamos a guardar los datos 
    #dichos anteriormente, cabe recalcar que los fields de admin se llenan con el mismo nombre
    #con categoria es lo mismo

    def __str__(self, ):
        return self.producto + "---" + str(self.fecha_de_publicacion)
    categoria = models.ManyToManyField(Categoria) 
       #este metodo str nos permite mostrar el nombre que le ponemos en el sitio admin de la pagina web
    


 


 

   


