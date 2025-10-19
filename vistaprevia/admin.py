

# Register your models here.
from django.contrib import admin 
from vistaprevia.models import Categoria
from vistaprevia.models import Producto


class Productoinline(admin.TabularInline):
    model = Producto
    extra = 0

   

class CategoriaAdmin(admin.ModelAdmin):
    inlines = [Productoinline]

"""admin register relaciona productoadmin con producto"""
@admin.register(Producto)
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

    list_display = ["producto","fecha_de_publicacion","imagen","Estado", "upper_case_name"]
    #list display lo que permite es mostrar la descripcion o lo que guardamos en las variables ej
    #tipo de producto, categoria, fehca de publicacion estado etc

    ordering = ["-fecha_de_publicacion","estado"]

    #UNA LISTA QUE PERMITE LOS CAMPOS POR LOS CUALES QUIERO ORDENAR MI APLICACION

    list_filter = ["categoria","fecha_de_publicacion","estado"]

    #nos virve para filtrar las cosas que queremos buscar en admin

    list_display_links=("producto","fecha_de_publicacion",)

    @admin.display(description='Name')
    def upper_case_name(self,obj):
        return("%s %s" % (obj.producto, obj.estado)).upper()
    
        
    #list display links nos permite ingresar a modificar el producto desde la fecha de publicacion h otra cosa

    """admin display sirve para customziar el panel de administracion con list display
    en este caso el metodo dice que toma los objetos(productos), sus nombres los pone en mayuscula
     una ves que hacemos esta funcion upper_case_name la tenemos que agregar en list_displays """

"""admin.site.register(Producto, ProductoAdmin)"""
#el admin site register nos sirve para que aparezca esa opcion en el panel admin de la pagina web
"""podes usar admin.site.register o usar el decorador para relacionar producto y producto admin
ahora esta puesto el decorador"""
admin.site.register(Categoria,CategoriaAdmin)
"""admin.site.register(Categoria)"""