from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.
class Estado(models.Model):
    ESTADO_OBRA_CHOICES =(
        ('Aprobado', 'Aprobado'),
        ('Pendiente', 'Pendiente'),
        ('Rechazado', 'Rechazadp')
    )
    idEstado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=255, choices=ESTADO_OBRA_CHOICES,default=1)
    
    def __str__(self):
        return str(self.estado)
    
class Obras(models.Model):
    TIPO_OBRA_CHOICES = (
        ('pintura', 'Pintura'),
        ('escultura', 'Escultura'),
    )
    idObras = models.AutoField(primary_key=True)
    Obras = models.CharField(max_length=255)
    descripcion = models.TextField(default="")
    imagen = models.ImageField(upload_to='Img/')
    idUsuario = models.ForeignKey(User,on_delete=models.CASCADE)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE,default=1)
    tipo = models.CharField(max_length=10, choices=TIPO_OBRA_CHOICES, default=1)

    def __str__(self):
        return str(self.Obras)