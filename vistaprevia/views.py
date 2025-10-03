from django.shortcuts import render
from django.http import HttpResponse


"""
def index(reques):
    return HttpResponse("hola mundo")


"""

def index(reques):
    paraams = {"nombresitio":"librosonline"}

    return render(reques, "vistaprevia/index.html", paraams)