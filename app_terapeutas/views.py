from django.shortcuts import render, redirect, get_object_or_404
from .models import Terapeuta

# Listar terapeutas
def index(request):
    terapeutas = Terapeuta.objects.all()
    return render(request, 'listar_terapeutas.html', {'terapeutas': terapeutas})

# Ver terapeuta (opcional, puedes usarlo si quieres detalle)
def ver_terapeuta(request, id):
    terapeuta = get_object_or_404(Terapeuta, id=id)
    return render(request, 'ver_terapeuta.html', {'terapeuta': terapeuta})

# Agregar terapeuta
def agregar_terapeuta(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        Terapeuta.objects.create(nombre=nombre, apellido=apellido, correo=correo, telefono=telefono, direccion=direccion)
        return redirect('lista_terapeutas')
    return render(request, 'agregar_terapeuta.html')

# Editar terapeuta
def editar_terapeuta(request, id):
    terapeuta = get_object_or_404(Terapeuta, id=id)
    if request.method == 'POST':
        terapeuta.nombre = request.POST['nombre']
        terapeuta.apellido = request.POST['apellido']
        terapeuta.correo = request.POST['correo']
        terapeuta.telefono = request.POST['telefono']
        terapeuta.direccion = request.POST['direccion']
        terapeuta.save()
        return redirect('lista_terapeutas')
    return render(request, 'editar_terapeuta.html', {'terapeuta': terapeuta})

# Borrar terapeuta
def borrar_terapeuta(request, id):
    terapeuta = get_object_or_404(Terapeuta, id=id)
    if request.method == 'POST':
        terapeuta.delete()
        return redirect('lista_terapeutas')
    return render(request, 'borrar_terapeuta.html', {'terapeuta': terapeuta})
