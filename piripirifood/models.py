from django.conf import settings
from django.db import models
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

class Categoria(models.Model):

    nome_categoria  = models.CharField(max_length=200)
    ativo_categoria = models.BooleanField(default=True)

    def __str__(self):
        return 'Categoria: {}'.format(self.nome_categoria)

class Estabelecimento(models.Model):
    nome_estabelecimento                = models.CharField(max_length=200, blank=False, null=False)
    categoria_estabelecimento           = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=False, null=False)
    longitude_estabelecimento           = models.DecimalField(max_digits=22, decimal_places=8, blank=False, null=False)
    latitude_estabelecimento            = models.DecimalField(max_digits=22, decimal_places=8, blank=False, null=False)
    logradouro_estabelecimento          = models.CharField(max_length=200, blank=False, null=False)
    numero_logradouro_estabelecimento   = models.CharField(max_length=200, blank=False, null=False)
    bairro_estabelecimento              = models.CharField(max_length=200, blank=False, null=False)
    telefone_estabelecimento            = models.CharField(max_length=14, blank=False, null=False)
    ativo_estabelecimento               = models.BooleanField(default=True)
    main_Picture_estabecimento          = models.ImageField(upload_to='estabelecimentoImagens/', storage=gd_storage, blank=False, null=False)
    picture01_estabecimento             = models.ImageField(upload_to='estabelecimentoImagens/', storage=gd_storage, blank=True, null=True)
    picture02_estabecimento             = models.ImageField(upload_to='estabelecimentoImagens/', storage=gd_storage, blank=True, null=True)
    picture03_estabecimento             = models.ImageField(upload_to='estabelecimentoImagens/', storage=gd_storage, blank=True, null=True)
    picture04_estabecimento             = models.ImageField(upload_to='estabelecimentoImagens/', storage=gd_storage, blank=True, null=True)

    def __str__(self):
        return 'Estabelecimento: {}'.format(self.nome_estabelecimento)