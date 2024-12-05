from django.db import models
from produtos.consts import *

class Produtos(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=600)
    estado = models.SmallIntegerField(choices=OPCOES_ESTADO)
    categoria = models.SmallIntegerField(choices=OPCOES_CATEGORIAS)
    foto = models.ImageField(blank=True, null=True, upload_to='produtos/fotos')
