from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from cadastro.models import Usuario
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
    usuario = request.user.id
    print(usuario)
    data_favoritos = Favorito.objects.filter(usuario_id=usuario)
    print()
    return render(request, 'perfil_usuário_favoritos.html', {'data_favoritos': data_favoritos})