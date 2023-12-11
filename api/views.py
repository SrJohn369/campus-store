from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from cadastro.models import Vendedor as VendedorModel
from cadastro.models import Usuario as UsuarioModel
from cadastro.models import Produto as ProdutoModel
from perfil.models import Favorito as FavoritoModel

from .serializers import *


# Create your views here.
@api_view(['GET'])
def index(request):
    vendedor = VendedorModel.objects.all()
    serializar_vendedor = VendedorSerializer(vendedor, many=True)
    
    return Response(serializar_vendedor.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'DELETE'])
def favoritar(request):
    if request.method == 'GET':
        favorito = FavoritoModel.objects.filter(usuario=request.user)
        serializar_favorito = Favoritos(favorito, many=True)
        serializar_usuario = UsuarioId(request.user)

        return Response({'favoritos':serializar_favorito.data,
                        'usuario': serializar_usuario.data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data
        print(data)
        
        produto = ProdutoModel.objects.get(id=data["produto_favorito"])
        usuario = UsuarioModel.objects.get(id=data['usuario'])
        
        FavoritoModel.objects.create(
            usuario=usuario,
            produto_favorito=produto
        )
        return Response({'html': 'deu bom'}, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        FavoritoModel.objects.delete(id=favorito)
        return Response({'mensagem': 'deletado com sucesso!'}, status=status.HTTP_200_OK)
