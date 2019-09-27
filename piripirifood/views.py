from django.shortcuts import render

from rest_framework import generics
from .models import Categoria
from .models import Estabelecimento
from .serializers import CategoriaSerializer
from .serializers import EstabelecimentoSerializer

# Create your views here.
class CategoriaList(generics.ListCreateAPIView):

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class EstabelecimentoList(generics.ListCreateAPIView):

    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer