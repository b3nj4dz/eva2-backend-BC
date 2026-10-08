from django.urls import path
from . import views

app_name="home"

urlpatterns = [
    path('', views.home, name='home'),
    path('peliculas/', views.pelis, name='peliculas'),
    path('accion/', views.accion, name='accion'),
    path('comedia/', views.comedia, name='comedia'),
    path('drama/', views.drama, name='drama'),
]