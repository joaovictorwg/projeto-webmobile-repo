from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from produtos.models import Produtos
from produtos.consts import OPCOES_ESTADO, OPCOES_CATEGORIAS  # Certifique-se de importar suas opções

class SerializadorProdutos(serializers.ModelSerializer):
    """
    Serializador para modelo de produto
    """
    nome_estado = serializers.SerializerMethodField()
    nome_categoria = serializers.SerializerMethodField()
    foto = Base64ImageField(required=False, represent_in_base64=True)

    class Meta:
        model = Produtos
        exclude = []  # Ou você pode incluir campos se desejar, como 'foto'

    def get_nome_estado(self, instancia):
        # Retorna o nome do estado com base nas opções definidas em OPCOES_ESTADO
        return dict(OPCOES_ESTADO).get(instancia.estado)

    def get_nome_categoria(self, instancia):
        # Retorna o nome da categoria com base nas opções definidas em OPCOES_CATEGORIAS
        return dict(OPCOES_CATEGORIAS).get(instancia.categoria)
