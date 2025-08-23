from django.db import models

# Create your models here.
# Modelos de los servicios prestados

class Service(models.Model):

    title = models.CharField(verbose_name='Título', max_length=200)
    subtitle = models.CharField(verbose_name='Subtítulo', max_length=200)
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen',upload_to='services/%Y/%m')
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Última edición',auto_now=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    
    def __str__(self):
        return self.title
