from django.db import models
from django.utils.html import format_html 

# Create your models here.
#cada vez que agregamos una variable aca tenemos que hacer un python manage.py makemigrations
#y luego python manage.py migrate
class Categoria(models.Model): 

    nombre = models.CharField(max_length=100, db_index=True) 

    slug = models.SlugField(max_length=100, db_index=True) 

 

    def __str__(self): 

        return '%s' % self.nombre 


class Producto(models.Model):

    borrador = "borrador"
    publicado = "publicado"
    retirado = "retirado"
    APROBACION_PRODUCTO = (
        (borrador,"borrador"),
        (publicado,"publicado"),
        (retirado,"retirado"),
    )
    #aca arriba nosotros ponemos la lista de estaods disponibles y abajo en la variable estado guardamos
    #el que elijamos, cabe recalcar que con choices eleijimos la lista
    estado= models.CharField(max_length=10, choices=APROBACION_PRODUCTO, default= "borrador")
    producto = models.CharField(max_length= 200)
    fecha_de_publicacion = models.DateTimeField('Fecha de publicacion')
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", blank=True, null=True) 

    #producto, fecha de publicacion e imagen nos sirven como variables donde vamos a guardar los datos 
    #dichos anteriormente, cabe recalcar que los fields de admin se llenan con el mismo nombre
    #con categoria es lo mismo
    """    categoria = models.ManyToManyField(Categoria) """
    """categoria para n a m """
    categoria = models.ForeignKey(
        Categoria, blank=False,null=True,on_delete=models.CASCADE
    )
    """cuando tenemos categorias 1 a n usamos el on delete"""


    def Estado(self):
        if self.estado == "retirado":
            return format_html('<span style="color: #f00;"> {} </span>', self.estado,)
        if self.estado == "borrador":
            return format_html('<span style="color: #f00;"> {} </span>', self.estado,)
        if self.estado == "publicado": 
            return format_html('<span style="color: #f00;"> {} </span>', self.estado,)
        
    #este metodo permite cambiarle el color en el cual aparece en admin

    """def __str__(self, ):
        return self.producto + "---" + str(self.fecha_de_publicacion)
    
       #este metodo str nos permite mostrar una descripcion de lo  que le ponemos en el sitio admin de la pagina web

       LO SACAMOS PORQUE PUSIMOS EN ADMIN LISTDISPLAY
    """



 


 

   


