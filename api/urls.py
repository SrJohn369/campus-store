from django.urls import path
from .views import *


app_name = 'api'

urlpatterns = [
    path("", index, name="index"),
    path("favoritar", favoritar, name="favoritar"),
    path("carrinho", carrinho, name="carrinho"),
    path("mudar_senha", mudar_senha, name="mudar_senha")
]
