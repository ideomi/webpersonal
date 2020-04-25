from django.db import models

# Create your models here.

class Service(models.Model):
    titulo=models.CharField(max_length=50,verbose_name='Título',null=True)
    subtitulo=models.CharField(max_length=25,verbose_name='Sub-título',null=True)
    contenido=models.TextField(verbose_name='Contenido',null=True)
    imagen=models.ImageField(verbose_name='Imagen',upload_to='services')
    creado=models.DateTimeField(auto_now_add=True,null=True,verbose_name='Creado')
    update=models.DateTimeField(auto_now=True,null=True,verbose_name='Ultima Actualización')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-creado']

    def __str__(self):
        return self.titulo

