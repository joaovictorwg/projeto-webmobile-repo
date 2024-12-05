from django.contrib.auth import get_user_model
from django.db import models
from produtos.models import Produtos

User = get_user_model()

# Create your models here.
class Anuncios(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=400)
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    foto = models.ImageField(upload_to='anuncios_imagens/', null=True, blank=True)

    produtos = models.ForeignKey(Produtos, related_name='anuncios', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, related_name='anuncios_realizados', on_delete=models.CASCADE)

    def __str__(self):
        return '{0} - {1} ({2})'.format(
            self.data,
            self.produtos,
            self.usuario
        )
    
    def save(self, *args, **kwargs):
        # Atribuir a imagem do produto ao anúncio, se houver uma imagem no produto
        if self.produtos.foto and not self.foto:
            self.foto = self.produtos.foto  # Copia a imagem do produto para o anúncio
        super(Anuncios, self).save(*args, **kwargs)