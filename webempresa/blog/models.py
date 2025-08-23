from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
# Modelos para la sección del blog
# Modelo Categoría

class Category(models.Model):
    name = models.CharField(verbose_name='Categoría', max_length=100)
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Fecha de edición', auto_now=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(verbose_name='Título', max_length=200)
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=now)
    image = models.ImageField(verbose_name='Imagen', null=True, blank=True, upload_to='blog/images/%Y/%m')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    categories = models.ManyToManyField(Category, verbose_name='Categorías', related_name="get_posts")
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Fecha de edición', auto_now=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
    
    def __str__(self):
        return self.title
    