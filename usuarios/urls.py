from usuarios import views
from django.urls import path

urlpatterns = [
    path('1/', views.index, name ="index")
    #aca tenemos el segundo par de urls en este caso solo para vistaprevia, lo que dice 
    #es que va air a views y de ahi busca la funcion index
]
