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
    
    # verificar usuario comprador
    if Usuario.objects.filter(username=user).exists():
        data_user = Usuario.objects.get(username=user)
        
        if request.method == 'GET':
            return render(request, 'perfil_usuário_perfil.html', {'data_user': data_user})
        
    # verificar usuario comprador
    elif Vendedor.objects.filter(username=user).exists():
        data_user = Vendedor.objects.get(username=user)
        
        if request.method == 'GET':
            return render(request, 'perfil_vendedor_perfil.html', {'data_user': data_user})
        
    else:
        if request.method == 'GET':
            return render(request, 'adm.html')
        

@login_required(login_url='login:login_usuario')
def logout_usuario(request):
    logout(request)
    return redirect('home:home')
            

@login_required(login_url='login:login_usuario')
def favoritos(request):
    if Usuario.objects.filter(username=request.user.username).exists():
        usuario = request.user.id
        favoritos = Favorito.objects.filter(usuario_id=usuario)
        
        data_produtos_fav = [
            favorito.produto_favorito for favorito in favoritos
        ]
        
        return render(request, 'perfil_usuário_favoritos.html', {'data_favoritos': data_produtos_fav})
        
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
        # Editar info do Usuario comprador
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
            if request.FILES.get('input-file'): # verifica se há arquivo
                user.foto = list_data[4]
                caminho_foto_antiga = user.foto.path
                if os.path.exists(caminho_foto_antiga):
                    os.remove(caminho_foto_antiga)
            
            # Atualiza dados
            user.first_name = list_data[0]
            user.last_name = list_data[1]
            user.email = list_data[2]
            user.telefone = list_data[3]
            
            user.save() 
            
            return render(request, 'sucesso_perfil.html')
        
        # Editar info do usuário vendedor
        elif Vendedor.objects.filter(username=request.user.username).exists():
            pass


@login_required(login_url='login:login_usuario')
def carrinho(request):
    if request.method == 'GET':
        usuario = request.user.id
        carrinho = Carrinho.objects.select_related(
            'produto__vendedor').filter(usuario__id=usuario)

        data_carrinho = [
            {
                'produto_nome': carrinho.produto.nome_prod,
                'produto_id': carrinho.produto.id,
                'produto_preço': carrinho.produto.preco,
                'vendedor_negocio': carrinho.produto.vendedor.negocio,
                'produto_quantidade': carrinho.quantidade_produto,
                'produto_foto': carrinho.produto.foto_prod,
                'carrinho_id': carrinho.id
            }
            for carrinho in carrinho
        ]
        # print(data_carrinho)
        return render(request, 'perfil_usuário_carrinho.html', {'data_carrinho': data_carrinho})
    
    if request.method == 'POST':
        pass


@login_required(login_url='login:login_usuario')
def produto(request):
    if request.method == 'GET':
        data_produtos = Produto.objects.filter(vendedor_id=request.user.id)
        print(Produto.objects.filter(vendedor_id=request.user))
        for a in Produto.objects.all():
            print(a)
        print(request.user.id)

        return render(request, "perfil_vendedor_prod.html", {'data_produtos': data_produtos})


@login_required(login_url='login:login_usuario')
def servico(request): 
    if request.method == 'GET': return render(request, 'servico.html')

        
@login_required(login_url='login:login_usuario')      
def sucesso(request):
    if request.method == 'GET': return render(request, 'sucesso.html')
    

@login_required(login_url='login:login_usuario') 
def config_vendedor(request):
    if request.method == 'GET': return render(request, 'configuracaov.html')


@login_required(login_url='login:login_usuario') 
def config_usuario(request):
    if request.method == 'GET': return render(request, 'configuracao.html')


@login_required(login_url='login:login_usuario')
def mudar_senhav(request):
    if request.method == 'GET': return render(request, 'mudar_senhav.html')
    
    
@login_required(login_url='login:login_usuario')
def mudar_senha_usuario(request):
    if request.method == 'GET': return render(request, 'mudar_senha_usuario.html')


@login_required(login_url='login:login_usuario')
def add_servico(request):
    if request.method == 'GET': return render(request, 'add_servico.html')
    

@login_required(login_url='login:login_usuario')
def editar_servico(request):
    if request.method == 'GET': return render(request, 'editar_servico.html')
    

@login_required(login_url='login:login_usuario')
def add_produto(request):
    if request.method == 'GET': return render(request, 'add_produto.html')


@login_required(login_url='login:login_usuario')
def editar_produto(request):
    if request.method == 'GET': return render(request, 'editar_produto.html')


@login_required(login_url='login:login_usuario')
def editar_perfil_vendedor(request):
    if request.method == 'GET': return render(request, 'editar-perfil-vendedor.html')
