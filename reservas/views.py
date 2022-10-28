
from django.shortcuts import render,redirect
from reservas.models import Reserva
from reservas.forms import Form_reserva

# Create your views here.

def index(request):
    return render(request, 'mostrar_reservas.html')

def listado_reservas(request):
    reserva = Reserva.objects.all()
    data = {'reservas': reserva}
    return render(request, 'mostrar_reservas.html', data)

def crear_reserva(request):
    form = Form_reserva()
    if request.method == 'POST':
        form = Form_reserva(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregar_reserva.html', data)

def eliminar_reserva(request,id):
    pro = Reserva.objects.get(id = id)
    pro.delete()
    return redirect('/')

def actualizar_reserva(request,id):
    pro = Reserva.objects.get(id = id)
    form = Form_reserva(instance=pro)
    if request.method == 'POST':
        form = Form_reserva(request.POST, instance=pro)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form':form}
    return render(request,'agregar_reserva.html',data)