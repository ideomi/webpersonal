from django.db import models
from ckeditor.fields import RichTextField

class Pages(models.Model):
    title=models.CharField(max_length=50,verbose_name='Título',null=True)
    content=RichTextField(verbose_name='Contenido',null=True)
    order = models.SmallIntegerField(verbose_name='Orden', default=0)
    creado=models.DateTimeField(auto_now_add=True,null=True,verbose_name='Creado')
    update=models.DateTimeField(auto_now=True,null=True,verbose_name='Ultima Actualización')

    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Paginas'
        ordering = ['order','title']

    def __str__(self):
        return self.title
