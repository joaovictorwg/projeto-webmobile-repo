# projeto-webmobile
Repositorio projeto final webmobile

# Configurar ambiente virtual
python -m venv venv
source venv/bin/activate (ou venv\Scripts\activate no Windows)

# Instalar Django
pip install django

# Criar projeto e app
django-admin startproject nome_do_projeto .
python manage.py startapp nome_do_app

# Executar migrações e servidor
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# Gerar/atualizar arquivo requirements.txt
pip freeze > requirements.txt

# Instalar dependências de requirements.txt
pip install -r requirements.txt

# Mobile
ionic start nome-do-projeto