from django.urls import path
from . import views
    
urlpatterns = [
    path('main', views.main, name='main'),
    path('login2', views.login2 , name='login2'),
    path('registro', views.registro , name='registro'),
    path('miguelangel', views.miguelangel , name='miguelangel'),
    path('pablopicasso', views.pablopicasso , name='pablopicasso'),
    path('vicentvangogh', views.vicentvangogh , name='vicentvangogh'),
    
    path('artista', views.artista , name='artista'),
    path('obras', views.obras , name='obras'),
    path('cerrar_sesion', views.cerrar_sesion , name='cerrar_sesion'),
    path('cambio_pass', views.cambio_pass , name='cambio_pass'),
    path('perfil', views.perfil , name='perfil'),
    path('todo', views.todo, name='todo'),
    
    path('agregarObra', views.agregarObra , name='agregarObra'),
    path('listaObra', views.listaObra , name='listaObra'),
    path('editarObra/<int:idObra>/', views.editarObra , name='editarObra'),
    path('actualizar_obra', views.actualizar_obra, name='actualizar_obra'),
    path('todo', views.todo, name='todo'),

    path('admin', views.admin , name='admin'),
]
