from django.contrib import admin
from produtos.models import Produtos

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'descricao', 'estado', 'categoria', 'foto']
    search_fields = ['modelo']

admin.site.register(Produtos, ProdutosAdmin)
