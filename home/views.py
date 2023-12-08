from django.shortcuts import render
from cadastro.models import Produto, Vendedor
from perfil.models import Avaliacao
from django.db.models import Avg


# Create your views here.
def home(request):
    # dados do produto + média de estrelas
    data_produto = Produto.objects.prefetch_related('avaliacao_set')\
        .annotate(media_avaliacao=Avg('avaliacao__estrelas')).all()
    
    if request.method == 'GET': return render(request, "home.html", {'data_protuto': data_produto})


def produtos(request):
    data_protuto_all = Produto.objects.all()

    if request.method == 'GET': return render(request, "produtos.html", {'data_protuto_all': data_protuto_all})


def vendedores(request):
    data_vendedor_all = Vendedor.objects.all()

    if request.method == 'GET': return render(request, "vendedores.html", {'data_vendedor_all': data_vendedor_all})

    