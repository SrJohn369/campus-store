from rest_framework import serializers
from cadastro.models import Vendedor, Produto, User
from perfil.models import Carrinho
from perfil.models import Favorito


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'
        

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome_prod', 'preco']


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # extra_kwargs = {'password': {'write_only': True}}


class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = '__all__'
        
        
class UsuarioId(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']
        # extra_kwargs = {'password': {'write_only': True}}


class Favoritos(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = [
            'id', 'produto_favorito', 'usuario'
        ]


class CarrinhoSerial(serializers.ModelSerializer):
    produto = ProdutoSerializer()
    class Meta:
        model = Carrinho
        fields = [
            'id', 'quantidade_produto', 'produto', 'usuario'
        ]