# Generated by Django 5.1.3 on 2024-11-29 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='estado',
            field=models.SmallIntegerField(choices=[(1, 'NOVO'), (2, 'USADO')]),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='produtos/fotos'),
        ),
    ]
