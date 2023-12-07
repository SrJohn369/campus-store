from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path("", views.perfil, name="perfil"),
    path('logout', views.logout_usuario, name="logout_usuario"),
    path('favoritos', views.favoritos, name="favoritos"),
    path('editar_informacoes', views.editar_informacoes, name="editar_informacoes"),
    path("carrinho", views.carrinho, name="carrinho"),
    path("produto_servico", views.produto_servico, name="produto_servico"),
    path('sucesso', views.sucesso, name='sucesso')
]
