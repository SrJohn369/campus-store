from rest_framework import serializers
from cadastro.models import Vendedor, Produto, Usuario, User
from perfil.models import Favorito


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'
        

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


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
        fields = ['id', 'produto_favorito', 'usuario']
