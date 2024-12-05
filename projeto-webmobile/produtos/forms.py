from django.forms import ModelForm
from produtos.models import Produtos

class FormularioProdutos(ModelForm):
    # Formulario para o model veiculo
    class Meta:
        model = Produtos
        exclude = []