from django.urls import path
from .views import *


app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('produtos', produtos, name='produtos'),
    path('vendedores', vendedores, name='vendedores'),
    path('pesquisa/<str:categoria>', pesquisa_categoria, name='pesquisa_categoria'),
    path('adicionar-ao-carrinho', adicionar_ao_carrinho, name='adicionar-ao-carrinho'),
    path('favoritar-produto', favoritar_produto, name='favoritar-produto'),
]
