from django.db import models

# Create your models here.


class Contenido(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    imagen = models.ImageField(upload_to='contenido_imagenes/')

    def __str__(self):
        return self.titulo
