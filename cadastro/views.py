from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def cadastro(request):
    return render(request, 'opc_cadastro.html')


def cadastro_sucesso(request):
    return render(request, 'sucesso.html')
    

def cadastro_usuario(request):
    if request.method == 'GET':
        return render(request, 'usuario_cadastrar.html')
    
    elif request.method == 'POST':
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
    
    
def cadastro_vendedor(request):
    if request.method == 'GET':
        return render(request, 'vendedor_cadastrar.html')
    
    elif request.method == 'POST':
        nome = request.POST.get('vendedor_nome')
        sobrenome = request.POST.get('vendedor_sobrenome')
        matricula = request.POST.get('vendedor_matricula')
        email = request.POST.get('vendedor_email')
        telefone = request.POST.get('vendedor_telefone')
        nome_negocio = request.POST.get('vendedor_nome_negocio')
        descricao_negocio = request.POST.get('vendedor_descricao_negocio')
        senha = request.POST.get('vendedor_senha')

        vendedor = Vendedor(
            firstname = nome,
            lastname = sobrenome,
            matricula = matricula,
            email = email,
            telefone = telefone,
            nome_negocio = nome_negocio,
            descricao_negocio = descricao_negocio,
            password = senha
        )
        try:
            vendedor.save()
            
            # confirmar dados
            return ('cadastro:sucesso')
        except:
            return HttpResponse('ERRO')
