from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path("", views.perfil, name="perfil"),
    path('logout/', views.logout_usuario, name="logout_usuario")
]
