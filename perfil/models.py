from django.db import models
from cadastro.models import *

class Favorito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    produto_favorito = models.ForeignKey(Produto, null=True, blank=True, on_delete=models.CASCADE)
    vendedor_favorito = models.ForeignKey(Vendedor, null=True, blank=True, on_delete=models.CASCADE)
    favoritado_em = models.DateTimeField(auto_now_add=True)


class Avaliacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, null=True, blank=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True, blank=True)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, null=True, blank=True)
    estrelas = models.IntegerField(null=True, blank=True)
    comentario = models.TextField(max_length=200, null=True, blank=True)
    avaliado_em = models.DateTimeField(auto_now_add=True)


class Carrinho(models.Model):
    
    quantidade_produto = models.IntegerField(blank=True, null=True)
    adicicionado_em = models.DateTimeField(auto_now_add=True)
    
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, blank=True, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)

    
class Compra(models.Model):
    
    Comprado_em = models.DateTimeField(auto_now_add=True)
    
    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True, related_name='comprador')
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, blank=True, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True, blank=True)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, null=True, blank=True)
    
    
class Parceria(models.Model):
    
    vendedor_parceiro = models.ForeignKey(Vendedor, on_delete=models.CASCADE, blank=True, null=True, related_name='parceiros')
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, blank=True, null=True)