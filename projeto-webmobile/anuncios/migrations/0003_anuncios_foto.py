# Generated by Django 5.1.3 on 2024-11-30 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0002_anuncios_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncios',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='anuncios_imagens/'),
        ),
    ]
