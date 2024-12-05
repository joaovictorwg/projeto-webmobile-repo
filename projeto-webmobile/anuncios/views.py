from django.shortcuts import render
from anuncios.models import Anuncios
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from anuncios.forms import FormularioAnuncios
from rest_framework import generics
from anuncios.models import Anuncios
from .serializers import SerializadorAnuncios
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404

# Create your views here.

class ListarAnuncios(LoginRequiredMixin, ListView):
    """
    View para listar anuncios cadastrados.
    """
    
    model = Anuncios
    context_object_name = 'anuncios'
    template_name = 'anuncios/listar.html'


class CriarAnuncios(LoginRequiredMixin, CreateView):
    model = Anuncios
    form_class = FormularioAnuncios
    template_name = 'anuncios/novo.html'
    success_url = reverse_lazy('listar-anuncios')


class EditarAnuncios(UpdateView):
    model = Anuncios
    form_class = FormularioAnuncios
    template_name = 'anuncios/editar.html'
    success_url = reverse_lazy('listar-anuncios')

    def get_object(self):
        # Garante que o objeto correto é editado
        return get_object_or_404(Anuncios, pk=self.kwargs['pk'])


class DeletarAnuncios(LoginRequiredMixin, DeleteView):
    model = Anuncios
    template_name = 'anuncios/deletar.html'
    success_url = reverse_lazy('listar-anuncios')

    def get_object(self):
        return get_object_or_404(Anuncios, pk=self.kwargs['pk'])

class APIListarAnuncios(generics.ListAPIView):
    """
    View para listar os anúncios cadastrados
    """
    queryset = Anuncios.objects.all()
    serializer_class = SerializadorAnuncios
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class APIDeletarAnuncios(generics.DestroyAPIView):
    """
    View para deletar anúncios
    """
    queryset = Anuncios.objects.all()
    serializer_class = SerializadorAnuncios
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class APICriarAnuncios(generics.CreateAPIView):
    """
    View para criar anúncios
    """
    queryset = Anuncios.objects.all()
    serializer_class = SerializadorAnuncios
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class APIEditarAnuncios(generics.UpdateAPIView):
    """
    View para editar anúncios
    """
    queryset = Anuncios.objects.all()
    serializer_class = SerializadorAnuncios
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]