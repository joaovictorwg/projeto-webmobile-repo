from django.urls import path
from anuncios.views import *


urlpatterns = [
    path('', ListarAnuncios.as_view(), name='listar-anuncios'),
    path('novo/', CriarAnuncios.as_view(), name='criar-anuncios'),
    path('<int:pk>/', EditarAnuncios.as_view(), name='editar-anuncios'),
    path('deletar/<int:pk>/', DeletarAnuncios.as_view(), name='deletar-anuncios'),
    # API urls
    path('api/', APIListarAnuncios.as_view(), name='api-listar-anuncios'),
    path('criar/', APICriarAnuncios.as_view(), name='api-criar-anuncio'),
    path('editar/<int:pk>/', APIEditarAnuncios.as_view(), name='api-editar-anuncio'),
    path('deletar/<int:pk>/', APIDeletarAnuncios.as_view(), name='api-deletar-anuncio'),
]