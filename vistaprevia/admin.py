

# Register your models here.
from django.contrib import admin 
from vistaprevia.models import Categoria
from vistaprevia.models import Producto

 
class ProductoAdmin(admin.ModelAdmin): 

    #fields =['producto','categoria', 'fecha_de_publicacion', 'imagen'] 
    #fields nos sirve para acomodar la posicion en la cual queremos ingresar datos

    fieldsets = [("relacion", {"fields":
                            ["categoria"]
                            }),
              ("datos generales",{"fields":
                                   ["producto", "fecha_de_publicacion", "imagen", "estado"] 
                                   },
                                        ),
                                            ]
    #fields set nos sirve para que en el admin nos agrupen los datos bajo un titulo
    #ej relacion va con cateroria y datos generales con producto....
    #lo que ponemos categoria,producto y los demas tienen que ser las variables que ponemos en models.py

    list_display = ["producto","fecha_de_publicacion","imagen","color_de_Estado"]
    #list display lo que permite es mostrar la descripcion o lo que guardamos en las variables ej
    #tipo de producto, categoria, fehca de publicacion estado etc

    ordering = ["-fecha_de_publicacion","estado"]

    #UNA LISTA QUE PERMITE LOS CAMPOS POR LOS CUALES QUIERO ORDENAR MI APLICACION

    list_filter = ["categoria","fecha_de_publicacion","estado"]

    #nos virve para filtrar las cosas que queremos buscar en admin

    list_display_links=("producto","fecha_de_publicacion",)
    #nos permite ingresar a modificar el producto desde la fecha de publicacion h otra cosa
 #el admin site register nos sirve para que aparezca esa opcion en el panel admin de la pagina web

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)