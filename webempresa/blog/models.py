from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class Categori(models.Model):
    name = models.CharField(max_length=50, verbose_name='categoria')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-created']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='Titulo')
    content = models.TextField(verbose_name='contenido')
    image =  models.ImageField(verbose_name='Imagen',upload_to='services')
    published = models.DateTimeField(verbose_name='Fecha de publicación',default=now)
    autor = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='autor')
    categori = models.ManyToManyField(Categori,verbose_name='Categoria',related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title