from django.urls import path
from .views import *


app_name = 'cadastro'

urlpatterns = [
    path('', cadastro, name='cadastro'),
    path('cadastro_usuario/', cadastro_usuario, name='cadastro_usuario'),
    path('cadastro_vendedor/', cadastro_vendedor, name='cadastro_vendedor'),
    path('cadastro_com_sucesso', cadastro_sucesso, name='sucesso')
]
