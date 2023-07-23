from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# category model
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural = 'Categorias'
        ordering =['name']

    def __str__(self):
        return self.name
    
# tag models
class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name='Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering =['name']

    def __str__(self):
        return self.name
    
# author models

# author models
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    excerpt = models.TextField(verbose_name='extracto')
    #content = models.TextField(verbose_name='Contenido')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='post', verbose_name='Imagen', null=True, blank=True)
    published = models.BooleanField(default=False, verbose_name='Publicado')

    #relationship
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_posts',verbose_name='Categoria')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_posts', verbose_name='Autor')
    tags = models.ManyToManyField(Tag, verbose_name='Etiquetas')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name='Publicacion'
        verbose_name_plural = 'Publicaciones'
        ordering =['-created']

    def __str__(self):
        return self.title
    
#ABOUT MODEL
class About(models.Model):
    description = models.CharField(max_length=400, verbose_name='Descripcion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name = 'Acerca de'
        verbose_name_plural = 'Acerca de Nosotros'
        ordering = ['-created']

    def __str__(self):
        return self.description
    
#SOCIAL MODEL
class Link(models.Model):
    key = models.CharField(max_length=100, verbose_name='Key Link')
    name = models.CharField(max_length=150, verbose_name="Red Social")
    url = models.URLField(max_length=350, blank=True, null=True, verbose_name='Enlace')
    icon = models.CharField(max_length=100, verbose_name='Icono', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
        ordering = ['name']

    def __str__(self):
        return self.name
        


