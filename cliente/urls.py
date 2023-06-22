from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main, name='main'),
    path('login', views.login , name='login'),
    path('login2', views.login2 , name='login2'),
    path('registro', views.registro , name='registro'),
    path('miguelangel', views.miguelangel , name='miguelangel'),
    path('pablopicasso', views.pablopicasso , name='pablopicasso'),
    path('vicentvangogh', views.vicentvangogh , name='vicentvangogh'),
    
    path('artista', views.artista , name='artista'),
    path('obras', views.obras , name='obras'),
    path('base', views.base , name='base'),
]
