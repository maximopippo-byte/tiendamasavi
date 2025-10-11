

# Register your models here.
from django.contrib import admin 
from vistaprevia.models import Categoria
from vistaprevia.models import Producto

 
class ProductoAdmin(admin.ModelAdmin): 

    fields =['producto','categoria', 'fecha_de_publicacion', 'imagen'] 

#fields nos sirve para acomodar la posicion en la cual queremos ingresar datos

 

 #el admin site register nos sirve para que aparezca esa opcion en el panel admin de la pagina web

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)