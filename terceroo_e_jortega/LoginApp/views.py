from django.shortcuts import render, redirect
from .models import Ciudades, Generos, Usuarios

def loguinDef(request):
    return render(request, 'login.html')

def registerDef(request):
    ciudades = Ciudades.objects.all()
    generos = Generos.objects.all()
    return render(request, 'register.html', {'ciudades': ciudades, 'generos': generos})

def registrarUsuarioDef(request):
    if request.method == 'GET':
        return redirect('register')
    else:
        nombre = request.POST['txtNombre']
        usuario = request.POST['txtUsuario']
        contra1 = request.POST['txtPassword1']
        contra2 = request.POST['txtPassword2']
        genero_id = request.POST['txtGenero']
        genero = Generos.objects.get(id=genero_id)
        ciudad_id = request.POST['txtCiudad']
        ciudad = Ciudades.objects.get(id=ciudad_id)
        correo = request.POST['txtCorreo']

        try:
            if contra1 != contra2:
                error_message = 'Las Contraseñas No Coinciden'
                ciudades = Ciudades.objects.all()
                generos = Generos.objects.all()
                return render(request, 'register.html', {'ciudades': ciudades, 'generos': generos, 'error_message': error_message})
            elif Usuarios.objects.filter(usuario=usuario).exists():
                error_message = 'El Usuario Ya Existe'
                ciudades = Ciudades.objects.all()
                generos = Generos.objects.all()
                return render(request, 'register.html',
                {'ciudades': ciudades, 'generos': generos, 'error_message': error_message})

            else:
                user = Usuarios.objects.create(
                    nombre=nombre,
                    correo=correo,
                    ciudad=ciudad,
                    genero=genero,
                    usuario=usuario,
                    contrasena=contra2
                )
                user.save()
                error_message = 'Registro Exitoso'
                ciudades = Ciudades.objects.all()
                generos = Generos.objects.all()
                return render(request, 'register.html', {'ciudades': ciudades, 'generos': generos, 'error_message': error_message})
        except:
            error_message = 'Ah Ocurrido Un Error Intentelo Mas Tarde'
            ciudades = Ciudades.objects.all()
            generos = Generos.objects.all()
            return render(request, 'register.html', {'ciudades': ciudades, 'generos': generos, 'error_message': error_message})

def loguearUsuarioDef(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        usuario = request.POST['txtUsuario']
        contrasena = request.POST['txtContrasena']

        try:
            user = Usuarios.objects.get(usuario=usuario)
            if user.contrasena == contrasena:
                request.session['user_id'] = user.id
                return redirect('inicio')
            else:
                error_message = 'Contraseña Incorrecta'
                return render(request, 'login.html', {'error_message': error_message})
        except Usuarios.DoesNotExist:
            error_message = 'El Usuario No Existe'
            return render(request, 'login.html', {'error_message': error_message})

