from django.shortcuts import get_object_or_404, render,redirect
from .models import Usuarios
from .form import UseForm
# Create your views here.

def list_usuarios(request):
    usu=  Usuarios.objects.all()
    
    return render(request, 'list_usuarios.html',{
        'usuarios': usu
    })

def create_user(request):
    usu = Usuarios(nombre=request.POST['nombre'],
             apellido=request.POST['apellido'],
             fecha_de_nacimiento=request.POST['fecha_nacimiento'],
             Genero=request.POST['genero'],
             direccion=request.POST['direccion'],
             estado_civil=request.POST['estado_civil'],
             dpi = request.POST['DPI']
             )
    usu.save()
    return redirect("list_usuarios")

def delete_usuarios(requets,user_id):
    usu = Usuarios.objects.get(id = user_id);
    usu.delete()
    return redirect("list_usuarios")
    
def update_usuarios(request, user_id):
    if request.method == "GET":
        usu = get_object_or_404(Usuarios, pk=user_id)
        form = UseForm( instance = usu)
        return render(request, 'actualizar_usuarios.html',{'usu':usu, 'form':form})
       
    else:
        usu = get_object_or_404(Usuarios, pk=user_id)
        form = UseForm(request.POST, instance = usu)
        form.save()
        return redirect("list_usuarios")
       


def cambiar_datos(request, user_id):
    if request.method == "GET":
        usu = get_object_or_404(Usuarios, pk=user_id)
        form = UseForm(instance = usu)
        return render(request, 'actualizar_usuarios.html',{'usu':usu, 'form':form})
       
    else:
        usu = get_object_or_404(Usuarios, pk=user_id)
        form = UseForm(request.POST, instance = usu)
        form.save()
        return redirect("list_usuarios")
       
