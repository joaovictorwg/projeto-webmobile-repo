from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.generic import View, CreateView, ListView, DeleteView, UpdateView
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from produtos.forms import FormularioProdutos
from produtos.models import Produtos
from produtos.serializers import SerializadorProdutos
from rest_framework import generics

# Create your views here.
class ListarProdutos(LoginRequiredMixin, ListView):
    # Views para listar produtos cadastrados
    model = Produtos
    context_object_name = 'produtos'
    template_name = 'produtos/listar.html'


class FotoProdutos(LoginRequiredMixin, View):
    def get(self, request, arquivo):
        try:
            produtos = Produtos.objects.get(foto='produtos/fotos/{}'.format(arquivo)) 
            return FileResponse(produtos.foto)
        except ObjectDoesNotExist as exc:
            raise Http404("Foto não encontrada") from exc
        except Exception as exception:
            raise exception

class CriarProdutos(LoginRequiredMixin, CreateView):
    model = Produtos
    form_class = FormularioProdutos
    template_name = 'produtos/novo.html'
    success_url = reverse_lazy('listar-produtos')

class EditarProdutos(LoginRequiredMixin, UpdateView):
    model = Produtos
    form_class = FormularioProdutos
    template_name = 'produtos/edit.html'
    success_url = reverse_lazy('listar-produtos')

class DeletarProdutos(LoginRequiredMixin, DeleteView):
    model = Produtos
    template_name = 'produtos/delete.html'
    success_url = reverse_lazy('listar-produtos')

    def get_object(self):
        return get_object_or_404(Produtos, pk=self.kwargs['pk'])
    
# API's -------------------------------------------------------------------------------------
    
class APIListarProdutos(ListAPIView):
    """
    view para listar instancias de produtos (por meio da API REST)
    """
    serializer_class = SerializadorProdutos
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Produtos.objects.all()
    
class APICriarProdutos(generics.CreateAPIView):
    """
    View para criar novos produtos via API.
    """
    queryset = Produtos.objects.all()
    serializer_class = SerializadorProdutos
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class APIEditarProdutos(generics.UpdateAPIView):
    """
    View para editar produtos via API.
    """
    queryset = Produtos.objects.all()
    serializer_class = SerializadorProdutos
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        # Recupera o produto a partir do ID da URL
        return Produtos.objects.get(pk=self.kwargs['pk'])

class APIDeletarProdutos(DestroyAPIView):
    """
    View para deletar instâncias de veículos (por meio da API REST)
    """
    serializer_class = SerializadorProdutos
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Produtos.objects.all()