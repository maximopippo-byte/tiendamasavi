from vistaprevia import views
from django.urls import path

urlpatterns = [
    path('1/', views.index, name ="vistaprevia1"),
    path('tienda/', views.shop, name ="tienda"),
    path("producto/<int:id>/", views.producto_detalle, name="producto_detalle")
    #aca tenemos el segundo par de urls en este caso solo para vistaprevia, lo que dice 
    #es que va air a views y de ahi busca la funcion index
]
