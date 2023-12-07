from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from .models import *

# Create your views here.
def cadastro(request):
    return render(request, 'opc_cadastro.html')


def cadastro_sucesso(request):
    return render(request, 'sucesso.html')
    

@csrf_protect
def cadastro_usuario(request):
    if request.method == 'GET':
        return render(request, 'usuario_cadastrar.html')
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        matricula = request.POST.get('matricula')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        senha = request.POST.get('senha')

        usuario = Usuario.objects.create_user(
            username=email,
            first_name=nome, last_name=sobrenome, 
            matricula=matricula, email=email, 
            telefone=telefone, password=senha)
        
        
        usuario.save()
        
        # confirmar dados
        return redirect('cadastro:sucesso')
    
    
@csrf_protect
def cadastro_vendedor(request):
    if request.method == 'GET':
        return render(request, 'vendedor_cadastrar.html')
    
    if request.method == 'POST':
        nome = request.POST.get('firstname')
        sobrenome = request.POST.get('lastname')
        matricula = request.POST.get('matricula')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        nome_negocio = request.POST.get('nome-negocio')
        descricao_negocio = request.POST.get('descricao_negocio')
        senha = request.POST.get('senha')

        vendedor = Vendedor.objects.create_user(
            first_name = nome,
            last_name = sobrenome,
            matricula = matricula,
            email = email,
            telefone = telefone,
            negocio = nome_negocio,
            username= email,
            descricao = descricao_negocio,
            password = senha,
        )
        
        vendedor.save() 
        # confirmar dados
        return redirect('cadastro:sucesso')
        
