from django.contrib import admin
from .models import Categoria
from .models import Estabelecimento
from .models import ImagemEstabelecimento

admin.site.register(Categoria)
admin.site.register(Estabelecimento)
admin.site.register(ImagemEstabelecimento)
