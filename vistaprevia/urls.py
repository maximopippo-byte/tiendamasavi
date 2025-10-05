from vistaprevia import views
from django.urls import path

urlpatterns = [
    path('1/', views.index, name ="index")
]
