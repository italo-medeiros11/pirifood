from django.conf import settings
from django.db import models

class Categoria(models.Model):
    nome_categoria  = models.CharField(max_length=200)
    ativo_categoria = models.BooleanField(default=True)

    def __str__(self):
        return 'Categoria: {}'.format(self.nome_categoria)

class Estabelecimento(models.Model):
    nome_estabelecimento                = models.CharField(max_length=200)
    categoria_estabelecimento           = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    longitude_estabelecimento           = models.DecimalField(max_digits=22, decimal_places=16, default=0.0)
    latitude_estabelecimento            = models.DecimalField(max_digits=22, decimal_places=16, default=0.0)
    logradouro_estabelecimento          = models.CharField(max_length=200,default='')
    numero_logradouro_estabelecimento   = models.CharField(max_length=200,default='')
    bairro_estabelecimento              = models.CharField(max_length=200,default='')
    telefone_estabelecimento            = models.CharField(max_length=14,default='')
    ativo_estabelecimento               = models.BooleanField(default=True)

    def __str__(self):
        return 'Estabelecimento: {}'.format(self.nome_estabelecimento)

class ImagemEstabelecimento(models.Model):
    url_imagemEstab             =  models.CharField(max_length=200)
    estabecimento_imagemEstab   = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    ativo_imagemEstab           = models.BooleanField(default=True)

    def __str__(self):
        return 'ImagemEstabelecimento: {}'.format(self.nome_estabelecimento)
