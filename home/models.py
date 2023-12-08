from django.db import models
from cadastro.models import Produto

# Create your models here.
class Categoria(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    
class Artesanato(Categoria):
    pass
class Doce(Categoria):
    pass
class Moda(Categoria):
    pass
class Salgado(Categoria):
    pass
class Bebida(Categoria):
    pass
class Gelado(Categoria):
    pass