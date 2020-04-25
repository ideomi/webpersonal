# Generated by Django 2.0.2 on 2020-04-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-creado'], 'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
        migrations.RemoveField(
            model_name='service',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='service',
            name='nombre',
        ),
        migrations.AddField(
            model_name='service',
            name='contenido',
            field=models.TextField(null=True, verbose_name='Contenido'),
        ),
        migrations.AddField(
            model_name='service',
            name='subtitulo',
            field=models.CharField(max_length=25, null=True, verbose_name='Sub-título'),
        ),
        migrations.AddField(
            model_name='service',
            name='titulo',
            field=models.CharField(max_length=50, null=True, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='service',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='service',
            name='imagen',
            field=models.ImageField(upload_to='services', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='service',
            name='update',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Ultima Actualización'),
        ),
    ]