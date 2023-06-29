# Generated by Django 4.1.2 on 2023-06-28 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id_tipo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='obras',
            name='imagen',
            field=models.ImageField(upload_to='Img/'),
        ),
        migrations.AddField(
            model_name='obras',
            name='tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cliente.tipo'),
        ),
    ]
