from django.contrib import admin
from anuncios.models import Anuncios


# Register your models here.
class AnunciosAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'descricao', 'produtos', 'usuario', 'preco']
    search_fields = ['descricao','produtos_modelo','usuario']

admin.site.register(Anuncios, AnunciosAdmin)