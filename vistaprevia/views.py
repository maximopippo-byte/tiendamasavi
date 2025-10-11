from django.shortcuts import render
from django.http import HttpResponse


"""
def index(reques):
    return HttpResponse("hola mundo")


"""

def index(reques):
    paraams = {"nombresitio":"librosonline"}

    return render(reques, "vistaprevia/index.html", paraams)
#en index lo que sucede es que tenemos el render que señala que tenemos que usar un hhtml, y vistaprevia/index.html
#nos indica donde el flamework tiene que ir a buscar el html
#cabe recalcar que antes tenemos que modificar seting la parte de template espeficicamente DIRS
#una ves que modificamos dirs  le agregamos una carpeta llamada template para que busque, en esa carpeta
#creamos otra carpeta llamada vistaprevia y creamos el archivo index.html