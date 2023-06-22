# Generated by Django 4.1.2 on 2023-06-22 00:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('idEstado', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Obras',
            fields=[
                ('idObras', models.AutoField(primary_key=True, serialize=False)),
                ('Obras', models.CharField(max_length=255)),
                ('descripcion', models.TextField(default='')),
                ('imagen', models.ImageField(upload_to='img/')),
                ('estado', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cliente.estado')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
