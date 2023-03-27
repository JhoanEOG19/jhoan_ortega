from django.shortcuts import render, redirect
from .models import Carros, Marcas
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def buscar_carros(request):
    query = request.GET.get('q')
    carro = Carros.objects.filter(
        Q(modelo__icontains=query) |
        Q(descripcion__icontains=query) |
        Q(precio__icontains=query) |
        Q(marca__nombre__contains=query) |
        Q(disponibilidad__icontains=query)
    )
    return render(request, 'InicioCarros.html', {'carro': carro})

def inicioDef(request):
    carro = Carros.objects.all()
    return render(request, 'InicioCarros.html', {'carro': carro})

def crearCarroDef(request):
    marca = Marcas.objects.all()
    return render(request, 'GestionarCarros.html', {'marca': marca})

def registrarCarroDef(request):
    id = request.POST['txtId']
    modelo = request.POST['txtModelo']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    marca_id = request.POST['txtMarca']
    marca = Marcas.objects.get(id=marca_id)
    disponibilidad = request.POST['txtDisponibilidad']

    try:
        carro = Carros.objects.create(
            id=id, modelo=modelo,
            descripcion=descripcion,
            precio=precio,
            disponibilidad=disponibilidad,
            marca=marca)
        messages.success(request, 'Carro Añadido Correctamente.')
        return render(request, 'GestionarCarros.html', {'mensaje_tipo': 'success', 'mensaje_texto': 'Carro Añadido Correctamente.'})

    except:
        messages.error(request, 'Ocurrió un error durante el registro. Por favor revise, inténtelo de nuevo.')
        return render(request, 'GestionarCarros.html', {'mensaje_tipo': 'error', 'mensaje_texto': 'Ocurrió un error durante el registro. Por favor revise, inténtelo de nuevo.'})

def editarCarroDef(request, id):
    carro = Carros.objects.get(id=id)
    marca = Marcas.objects.all()
    return render(request, 'EditarCarros.html', {'carro': carro, 'marca': marca})

def edicionCarroDef(request):
    id = request.POST['txtId']
    modelo = request.POST['txtModelo']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    disponibilidad = request.POST['txtDisponibilidad']

    carro = Carros.objects.get(id=id)
    carro.modelo = modelo
    carro.descripcion = descripcion
    carro.precio = precio
    carro.disponibilidad = disponibilidad
    carro.save()


    return redirect('inicio')

def borraCarroDef(request, id):
    carro = Carros.objects.get(id=id)
    carro.delete()
    return redirect('inicio')