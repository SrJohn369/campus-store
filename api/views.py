from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from cadastro.models import Vendedor as VendedorModel
from cadastro.models import Usuario as UsuarioModel
from cadastro.models import Produto as ProdutoModel
from perfil.models import Favorito as FavoritoModel
from perfil.models import Carrinho as CarrinhoModel

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
        
        if not request.user.is_authenticated:
            favorito = FavoritoModel()
            usuario = UsuarioModel()
            
            serializar_favorito = Favoritos(favorito)
            serializar_usuario = UsuarioId(usuario)

            return Response({'favoritos':serializar_favorito.data,
                            'usuario': serializar_usuario.data}, status=status.HTTP_200_OK)
        
        elif request.user.is_authenticated:
            favorito = FavoritoModel.objects.filter(usuario=request.user.id)
            
            serializar_favorito = Favoritos(favorito, many=True)
            serializar_usuario = UsuarioId(request.user)

            return Response({'favoritos':serializar_favorito.data,
                            'usuario': serializar_usuario.data}, status=status.HTTP_200_OK)
            
        return Response({'mensagem': 'DEU RUIM'}, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'POST':
        data = request.data
        print(data)
        
        produto = ProdutoModel.objects.get(id=data["produto_favorito"])
        usuario = UsuarioModel.objects.get(id=data['usuario'])
        
        FavoritoModel.objects.create(
            usuario=usuario,
            produto_favorito=produto
        )
        return Response({'mensagem': 'DEU BOM'}, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        favorito_id = request.query_params.get('favorito')
        
        if favorito_id:
            try:
                favorito = FavoritoModel.objects.get(id=favorito_id)
                favorito.delete()
                return Response({'mensagem': 'Removido dos favoritos com sucesso!'}, status=status.HTTP_200_OK)
            except FavoritoModel.DoesNotExist:
                return Response({'mensagem': 'Favorito não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'mensagem': 'Parâmetro favorito ausente.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def carrinho(request):
    if request.method == 'GET':
        
        if not request.user.is_authenticated:
            carrinho = CarrinhoModel()
            usuario = UsuarioModel()
            
            serializar_carrinho = CarrinhoSerial(carrinho)
            serializar_usuario = UsuarioId(usuario)

            return Response({'carrinho':serializar_carrinho.data,
                            'usuario': serializar_usuario.data}, status=status.HTTP_200_OK)
        
        elif request.user.is_authenticated:
            carrinho = CarrinhoModel.objects.filter(usuario=request.user.id)
            
            serializar_carrinho = CarrinhoSerial(carrinho, many=True)
            serializar_usuario = UsuarioId(request.user)

            return Response({'carrinho':serializar_carrinho.data,
                            'usuario': serializar_usuario.data}, status=status.HTTP_200_OK)
            
        return Response({'mensagem': 'DEU RUIM'}, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'POST':
        data = request.data
        print(data)
        
        produto = ProdutoModel.objects.get(id=data["produto"])
        usuario = UsuarioModel.objects.get(id=data['usuario'])
        
        CarrinhoModel.objects.create(
            usuario=usuario,
            produto=produto
        )
        return Response({'mensagem': 'DEU BOM'}, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        carrinho_id = request.query_params.get('carrinho')
        
        if carrinho_id:
            try:
                carrinho = CarrinhoModel.objects.get(id=carrinho)
                carrinho.delete()
                return Response({'mensagem': 'Removido dos favoritos com sucesso!'}, status=status.HTTP_200_OK)
            except CarrinhoModel.DoesNotExist:
                return Response({'mensagem': 'Favorito não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'mensagem': 'Parâmetro favorito ausente.'}, status=status.HTTP_400_BAD_REQUEST)
