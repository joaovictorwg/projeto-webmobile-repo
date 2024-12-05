from django.forms import ModelForm
from anuncios.models import Anuncios

class FormularioAnuncios(ModelForm):

    class Meta:
        model = Anuncios
        exclude = []