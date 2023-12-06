from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from cadastro.models import Usuario, Vendedor
from .models import *
import os


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
        
        try:    
            data_favoritos = Favorito.objects.filter(usuario_id=usuario)
            if data_favoritos:
                return render(request, 'perfil_usuário_favoritos.html', {'data_favoritos': data_favoritos})
            else:
                return render(request, 'perfil_usuário_favoritos.html', {'data_favoritos': 0})
        except:
            return render(request, 'perfil_usuário_favoritos.html', {'data_favoritos': 0})
        
    elif Vendedor.objects.filter(username=request.user.username).exists():
        usuario = request.user.id
        data_favoritos = Favorito.objects.filter(usuario_id=usuario)
        return render(request, 'perfil_usuário_favoritos.html', {'data_favoritos': data_favoritos})


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
                request.FILES.get('input-file')
            ]
            
            user = Usuario.objects.get(username=request.user.username)
            
            # Remove foto antiga
            caminho_foto_antiga = user.foto.path
            if os.path.exists(caminho_foto_antiga):
                os.remove(caminho_foto_antiga)
            
            # Atualiza dados
            user.first_name = list_data[0]
            user.last_name = list_data[1]
            user.email = list_data[2]
            user.telefone = list_data[3]
            user.foto = list_data[4]
            
            user.save() 
            
            return render(request, 'sucesso_perfil.html')
            
        elif Vendedor.objects.filter(username=request.user.username).exists():
            pass


@login_required(login_url='login:login_usuario')
def carrinho(request):
    if request.method == 'GET':
        
        dict_data = {} 
        
        try:
            data_carrinho = Carrinho.objects.filter(usuario=request.user.id)
            if data_carrinho:
                dict_data['data_carrinho'] = data_carrinho
            else:
                dict_data['data_carrinho'] = []
        except:
            dict_data['data_carrinho'] = []
        try:
            data_compras = Compra.objects.filter(usuario=request.user.id)
            if data_compras:
                dict_data['data_compras'] = data_compras
            else:
                dict_data['data_compras'] = []
        except:
            dict_data['data_compras'] = []
        
        return render(request, 'perfil_usuário_carrinho.html', dict_data)
    
    if request.method == 'POST':
        pass

        
@login_required(login_url='login:login_usuario')      
def sucesso(request):
    if request.method == 'GET': return render(request, 'sucesso.html')
