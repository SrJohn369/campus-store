from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Vendedor(User):
    
    matricula = models.CharField(primary_key=True, max_length=30, blank=False)
    telefone = models.CharField(max_length=20, blank=False, default='')
    foto = models.ImageField(default='foto_vendedor/imagem_usuario_padrão.jpg',
                             upload_to='foto_vendedor')
    negocio = models.CharField(max_length=30, blank=False)
    descricao = models.TextField(max_length=500, blank=True, default='Descrição do seu negócio.', null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Usuários Vendedore'
    
    
class Produto(models.Model):
    
    nome_prod = models.CharField(max_length=50, blank=False)
    descricao = models.TextField(max_length=150, blank=False)
    preco = models.DecimalField(max_digits=9, decimal_places=2, blank=False)
    foto_prod = models.ImageField(
        null=False, default='', upload_to='foto_produto')
    
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.nome_prod} - R${self.preco}'

    
    
class Servico(models.Model):
    
    tipo_serv = models.CharField(max_length=32, blank=False)
    descricao_serv = models.TextField(max_length=50, blank=False)
    
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return f'{self.tipo_serv} - {self.descricao_serv}'


class Usuario(User):
    matricula = models.CharField(max_length=30, blank=False, unique=True)
    telefone = models.CharField(max_length=20, blank=False, default='')
    foto = models.ImageField(upload_to='foto_usuario',
                             default='foto_usuario/imagem_usuario_padrão.jpg')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Usuários Compradore'
    
