from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from cadastro.models import Usuario, Vendedor
from .models import *


app_name = 'perfil'


# Create your views here.
@login_required(login_url='login:login_usuario')
def perfil(request):
    user = request.user.username
    data_user = Usuario.objects.get(username=user)
    
    if request.method == 'GET':
        return render(request, 'perfil_usuário_perfil.html', {'data_user': data_user})

@login_required(login_url='login:login_usuario')
def logout_usuario(request):
    logout(request)
    return redirect('home:home')
            

@login_required(login_url='login:login_usuario')
def favoritos(request):
    if Usuario.objects.filter(username=request.user.username).exists():
        usuario = request.user.id
        print(usuario)
        data_favoritos = Favorito.objects.filter(usuario_id=usuario)
        print()
        return render(request, 'perfil_usuário_favoritos.html', {'data_favoritos': data_favoritos})
    elif Vendedor.objects.filter(username=request.user.username).exists():
        usuario = request.user.id
        print(usuario)
        data_favoritos = Favorito.objects.filter(usuario_id=usuario)
        print()
        return render(request, 'perfil_usuário_favoritos.html', {'data_favoritos': data_favoritos})


@login_required(login_url='login:login_usuario')
def alterar_foto(request):
    pass


@login_required(login_url='login:login_usuario')
def editar_informacoes(request):
    user = request.user.username
    data_user = Usuario.objects.get(username=user)

    if request.method == 'GET':
        return render(request, 'editar_informacoes.html', {'data_user': data_user})
    
    elif request.method == 'POST':
        if Usuario.objects.filter(username=request.user.username).exists():
            list_data = [
                request.POST.get('text-nome'),
                request.POST.get('text-sobrenome'),
                request.POST.get('text-email'),
                request.POST.get('text-telefone'),
                request.POST.get('input-file')
            ]
            
            user = Usuario.objects.get(username=request.user.username)
            
            user.first_name = list_data[0]
            user.last_name = list_data[1]
            user.email = list_data[2]
            user.telefone = list_data[3]
            user.foto = list_data[4]
            
            user.save()
            
            return render(request, 'sucesso_perfil.html')
            
        elif Vendedor.objects.filter(username=request.user.username).exists():
            pass
        
        
def sucesso(request):
    if request.method == 'GET': return render(request, 'sucesso.html')
