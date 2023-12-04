from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from cadastro.models import Usuario


app_name = 'perfil'


# Create your views here.
@login_required(login_url='login:login_usuario')
def perfil(request):
    user = request.user.username
    data_user = Usuario.objects.get(username=user)
    
    if request.method == 'GET': return render(request, 'perfil_usuário.html', {'data_user': data_user})

@login_required(login_url='login:login_usuario')
def logout_usuario(request):
    logout(request)
    return redirect('home:home')
            

# @login_required(login_url='login:login_usuario')
# def favoritos(request):
#     return 