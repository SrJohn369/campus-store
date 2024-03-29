from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path("", views.perfil, name="perfil"),
    path('logout', views.logout_usuario, name="logout_usuario"),
    path('favoritos', views.favoritos, name="favoritos"),
    path('editar_informacoes', views.editar_informacoes, name="editar_informacoes"),
    path("carrinho", views.carrinho, name="carrinho"),
    path("produto_servico", views.produto, name="produto_servico"),
    path("servico", views.servico, name="servico"),
    path('sucesso', views.sucesso, name='sucesso'),
    path("configuracao_usario", views.config_usuario, name="config_usuario"),
    path("configuracao_vendedor", views.config_vendedor, name="config_vendedor"),
    path("mudar_senhav", views.mudar_senhav, name="mudar_senhav"),
    path("mudar_senha_usuario", views.mudar_senha_usuario, name="mudar_senha_usuario"),
    path("adicionar_servico", views.add_servico, name="add_servico"),
    path("editar_servico", views.editar_servico, name="editar_servico"),
    path("adicionar_produto", views.add_produto, name="add_produto"),
    path("editar_produto", views.editar_produto, name="editar_produto"),
    path("editar_perfil_vendedor", views.editar_perfil_vendedor, name="editar_perfil_vendedor"),
]
