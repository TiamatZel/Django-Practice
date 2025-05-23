# Generated by Django 5.2 on 2025-04-24 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateField()),
                ('descripcion', models.TextField(blank=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.autor')),
            ],
        ),
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('puntuacion', models.PositiveIntegerField(default=0)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.libro')),
            ],
        ),
    ]
