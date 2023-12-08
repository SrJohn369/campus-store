from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('produtos', produtos, name='produtos'),
    path('vendedores', vendedores, name='vendedores'),
    path('pesquisa/<str:categoria>', pesquisa_categoria, name='pesquisa_categoria')
]
