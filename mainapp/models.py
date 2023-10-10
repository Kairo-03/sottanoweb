from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class Contenido(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    imagen = models.ImageField(upload_to='contenido_imagenes/')

    def __str__(self):
        return self.titulo


class Usuario(AbstractBaseUser):
    username = models.CharField(
        'Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo', unique=True, max_length=254)
    nombres = models.CharField(
        'Nombres', max_length=200, blank=True, null=True)
    apellidos = models.CharField(
        'Apellidos', max_length=200, blank=True, null=True)
    imagen_de_perfil = models.ImageField(
        'Imagen de perfil', upload_to='perfil/', height_field=None, width_field=None, max_length=200)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']

    def __str__(self):
        return f'{self.nombres}, {self.apellidos}'

    def has_perm(self, perm, obj=None):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador
