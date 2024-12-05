from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Views de Login -------------------------------------------------------
class Login(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/produtos')
        return render(request, 'autenticacao/login.html')

    def post(self, request):
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Login bem-sucedido!')
                return redirect("/produtos")
            messages.error(request, 'Usuário inativo')
        else:
            messages.error(request, 'Usuário ou senha incorretos')

        return redirect('login')

class Logout(View):
    
    def get(self, request):
        logout(request)
        messages.info(request, 'Você foi desconectado.')
        return redirect(settings.LOGIN_URL)

# Views de register ---------------------------------------------------
class Register(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/produtos')
        return render(request, 'autenticacao/register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'As senhas não coincidem')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado')
            return redirect('register')

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('login')

class LoginAPI(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={
                'request': request
            }
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'id': user.id, 
            'nome': user.first_name,
            'email': user.email,
            'token': token.key
        })