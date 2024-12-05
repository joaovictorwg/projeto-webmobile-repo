from rest_framework import serializers
from anuncios.models import Anuncios
from produtos.serializers import SerializadorProdutos  # Certifique-se de que o serializador de Produtos está correto

class SerializadorAnuncios(serializers.ModelSerializer):
    """
    Serializador para o modelo Anuncios
    """
    produtos = SerializadorProdutos()  # Inclui os detalhes do produto no anúncio
    usuario = serializers.StringRelatedField()  # Exibe o nome do usuário ao invés do ID

    class Meta:
        model = Anuncios
        fields = ['id', 'data', 'titulo', 'descricao', 'preco', 'produtos', 'usuario', 'foto']
