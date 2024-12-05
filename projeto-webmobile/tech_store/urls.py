from django.contrib import admin
from django.urls import path
from tech_store.views import *
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('autenticacao-api/', LoginAPI.as_view()),
    path('logout/', Logout.as_view(), name='logout'),
    path('produtos/', include('produtos.urls'), name='produtos'),
    path('anuncios/', include('anuncios.urls'), name='anuncios'),

]
