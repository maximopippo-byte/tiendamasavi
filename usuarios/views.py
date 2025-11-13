from django.shortcuts import render

# Create your views here.

def index(reques):
    paraams = {"nombresitio":"librosonline"}

    return render(reques, "vistaprevia/index.html", paraams)