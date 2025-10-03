from vistaprevia import views
from django.urls import path

urlpatterns = [
    path('vista/', views.index, name ="index")
]
