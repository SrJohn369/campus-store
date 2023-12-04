from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from cadastro.models import *


# Create your views here.
@csrf_protect
def login_usuario(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        login_email = request.POST.get('email')
        login_senha = request.POST.get('senha')
        user = authenticate(username=login_email, password=login_senha)
        
        if user is not None:
            login(request, user)
            print('deu bom')
            return redirect('home:home')
        else:
            return HttpResponse(f'Senha incorreta \n {login_email} - {login_senha} \n {user}')
        
        
