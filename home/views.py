from django.shortcuts import render
from cadastro.models import Produto


# Create your views here.
def home(request):
    data_produto = Produto.objects.all()
    
    if request.method == 'GET': return render(request, "home.html", {'data_protuto': data_produto})
