from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from vistaprevia.models import Producto


"""
def index(reques):
    return HttpResponse("hola mundo")


"""

from .models import Producto

def index(request):
    productos = Producto.objects.all()
    return render(request, "vistaprevia/index.html", {
        "productos": productos
    })


def shop(request):
    productos = Producto.objects.all()
    categorias = ["Hombre", "Mujer", "Accesorios", "Ofertas"]

    context = {
        "productos": productos,
        "categorias": categorias
    }

    return render(request, "vistaprevia/shop.html", context)


def producto_detalle(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, "vistaprevia/shop-single.html", {"producto": producto})

#en index lo que sucede es que tenemos el render que señala que tenemos que usar un hhtml, y vistaprevia/index.html
#nos indica donde el flamework tiene que ir a buscar el html
#cabe recalcar que antes tenemos que modificar seting la parte de template espeficicamente DIRS
#una ves que modificamos dirs  le agregamos una carpeta llamada template para que busque, en esa carpeta
#creamos otra carpeta llamada vistaprevia y creamos el archivo index.html