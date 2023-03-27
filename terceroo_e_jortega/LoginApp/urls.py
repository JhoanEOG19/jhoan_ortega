from django.urls import path
from . import views

urlpatterns = [
    path('', views.loguinDef, name='loguin'),
    path('register/', views.registerDef, name='register'),
    path('registrarUsuario/', views.registrarUsuarioDef, name='registrarUsuario'),
    path('loguearUsuario/', views.loguearUsuarioDef, name='loguearUsuario'),
]
