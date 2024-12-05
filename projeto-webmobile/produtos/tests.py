from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from produtos.models import Produtos
from produtos.consts import OPCOES_ESTADO, OPCOES_CATEGORIAS
import tempfile

class ProdutosViewTestCase(TestCase):
    def setUp(self):
        # Configuração inicial
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.produto = Produtos.objects.create(
            nome="Produto Teste",
            descricao="Descrição do Produto Teste",
            estado=list(OPCOES_ESTADO.keys())[0],
            categoria=list(OPCOES_CATEGORIAS.keys())[0],
            foto=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        self.client.login(username='testuser', password='testpassword')

    def test_listar_produtos(self):
        response = self.client.get(reverse('listar-produtos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'produtos/listar.html')

    def test_criar_produtos(self):
        data = {
            "nome": "Novo Produto",
            "descricao": "Descrição do novo produto",
            "estado": list(OPCOES_ESTADO.keys())[0],
            "categoria": list(OPCOES_CATEGORIAS.keys())[0]
        }
        response = self.client.post(reverse('criar-produto'), data)
        self.assertEqual(response.status_code, 302)  # Redireciona após criação
        self.assertTrue(Produtos.objects.filter(nome="Novo Produto").exists())

    def test_editar_produtos(self):
        response = self.client.post(
            reverse('editar-produto', kwargs={"pk": self.produto.pk}),
            {"nome": "Produto Editado"}
        )
        self.assertEqual(response.status_code, 302)
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.nome, "Produto Editado")

    def test_deletar_produtos(self):
        response = self.client.post(reverse('deletar-produto', kwargs={"pk": self.produto.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Produtos.objects.filter(pk=self.produto.pk).exists())

class ProdutosAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.produto = Produtos.objects.create(
            nome="Produto API Teste",
            descricao="Descrição do Produto API",
            estado=list(OPCOES_ESTADO.keys())[0],
            categoria=list(OPCOES_CATEGORIAS.keys())[0]
        )

    def test_api_listar_produtos(self):
        response = self.client.get(reverse('api-listar-produtos'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) > 0)

    def test_api_criar_produtos(self):
        data = {
            "nome": "Novo Produto API",
            "descricao": "Descrição do novo produto API",
            "estado": list(OPCOES_ESTADO.keys())[0],
            "categoria": list(OPCOES_CATEGORIAS.keys())[0]
        }
        response = self.client.post(reverse('api-criar-produtos'), data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Produtos.objects.filter(nome="Novo Produto API").exists())

    def test_api_editar_produtos(self):
        data = {"nome": "Produto API Editado"}
        response = self.client.put(reverse('api-editar-produtos', kwargs={"pk": self.produto.pk}), data)
        self.assertEqual(response.status_code, 200)
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.nome, "Produto API Editado")

    def test_api_deletar_produtos(self):
        response = self.client.delete(reverse('api-deletar-produtos', kwargs={"pk": self.produto.pk}))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Produtos.objects.filter(pk=self.produto.pk).exists())
