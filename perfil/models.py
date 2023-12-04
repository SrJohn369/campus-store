from django.db import models
from ..cadastro.models import *

class Favorito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    favoritado_em = models.DateTimeField(auto_now_add=True)

class Avaliacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True, blank=True)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, null=True, blank=True)
    estrelas = models.IntegerField(null=True, blank=True)
    comentario = models.TextField(max_length=200, null=True, blank=True)
    avaliado_em = models.DateTimeField(auto_now_add=True)

