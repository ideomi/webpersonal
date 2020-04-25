from django.db import models

# Create your models here.

class Link(models.Model):
    key=models.SlugField(max_length=50,verbose_name='Clave',unique=True)
    name=models.CharField(max_length=25,verbose_name='Red social',null=True)
    url=models.URLField(verbose_name='URL',null=True)
    creado=models.DateTimeField(auto_now_add=True,null=True,verbose_name='Creado')
    update=models.DateTimeField(auto_now=True,null=True,verbose_name='Ultima Actualización')

    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['-name']

    def __str__(self):
        return self.name
