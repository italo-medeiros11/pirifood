from rest_framework import serializers
from .models import Categoria
from .models import Estabelecimento

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Categoria
        fields = '__all__'


class EstabelecimentoSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Estabelecimento
        fields = '__all__'