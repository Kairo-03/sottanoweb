from django.db import models
from django.contrib.auth.forms import UserCreationForm
# Create your models here.


class Contenido(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    imagen = models.ImageField(upload_to='contenido_imagenes/')

    def __str__(self):
        return self.titulo


class Avatar(models.Model):
    user = models.ForeignKey(
        UserCreationForm.Meta.model, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares/', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
