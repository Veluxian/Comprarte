# Generated by Django 4.1.2 on 2023-06-29 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_remove_obras_tipo_delete_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='obras',
            name='tipo',
            field=models.CharField(choices=[('pintura', 'Pintura'), ('escultura', 'Escultura')], default=1, max_length=10),
        ),
    ]