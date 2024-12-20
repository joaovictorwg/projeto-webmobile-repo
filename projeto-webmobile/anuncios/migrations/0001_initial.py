# Generated by Django 5.1.3 on 2024-11-29 19:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0002_alter_produtos_estado_alter_produtos_foto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('descricao', models.CharField(max_length=400)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('produtos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anuncios', to='produtos.produtos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anuncios_realizados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
