from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicioDef, name='inicio'),
    path('crearCarro/', views.crearCarroDef, name='crear'),
    path('registrarCarro/', views.registrarCarroDef, name='registrarCarro'),
    path('editarCarro/<int:id>', views.editarCarroDef, name='editarCarro'),
    path('edicionCarro/', views.edicionCarroDef, name='edicionCarro'),
    path('borrarCarro/<id>', views.borraCarroDef, name='borrarCarro'),
    path('buscar_carro/', views.buscar_carros, name='buscarcarro'),

]