from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from cadastro.models import Vendedor as VendedorModel

from .serializers import VendedorSerializer


# Create your views here.
@api_view(['GET'])
def index(request):
    vendedor = VendedorModel.objects.all()
    serializarvendedor = VendedorSerializer(vendedor, many=True)
    
    return Response(serializarvendedor.data, status=status.HTTP_200_OK)