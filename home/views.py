from django.shortcuts import render
from cadastro.models import Produto, Vendedor, Categoria
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Avg
from django.http import JsonResponse


# Create your views here.
def home(request):
    # dados do produto + média de estrelas
    data_produto = Produto.objects.prefetch_related('avaliacao_set')\
        .annotate(media_avaliacao=Avg('avaliacao__estrelas')).all()
    
    if request.method == 'GET': return render(request, "home.html", {'data_protuto': data_produto})


def produtos(request):
    # dados do produto + média de estrelas
    data_protuto_all = Produto.objects.prefetch_related('avaliacao_set')\
        .annotate(media_avaliacao=Avg('avaliacao__estrelas')).all()

    if request.method == 'GET': return render(request, "produtos.html", {'data_protuto_all': data_protuto_all})


def vendedores(request):
    data_vendedor_all = Vendedor.objects.all()

    if request.method == 'GET': return render(request, "vendedores.html", {'data_vendedor_all': data_vendedor_all})

    
def pesquisa_categoria(request, categoria):
    categoria_obj = Categoria.objects.get(nome=categoria.lower())

    result_categoria = Produto.objects.filter(categorias=categoria_obj)\
        .prefetch_related('avaliacao_set')\
        .annotate(media_avaliacao=Avg('avaliacao__estrelas'))

    if request.method == 'GET':
        return render(request, 'resultados.html', {'result_categoria': result_categoria})


@login_required(login_url='login:login_usuario')
def adicionar_ao_carrinho(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        # Lógica para adicionar o produto ao carrinho
        return JsonResponse({'mensagem': 'Produto adicionado ao carrinho com sucesso!'})


@login_required(login_url='login:login_usuario')
def favoritar_produto(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        # Lógica para favoritar o produto
        return JsonResponse({'mensagem': 'Produto favoritado com sucesso!'})
