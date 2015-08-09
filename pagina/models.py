# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Entrada(models.Model):
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering=['-fecha']

    imagen = models.FileField(u'Imagen del Post', upload_to='imagenesdepost', default='null')
    titulo = models.CharField(u'Título', max_length=100)
    fecha = models.DateTimeField(u'Fecha del Post',auto_now_add=True)
    resumen= models.CharField(u'Resumen',max_length=512)
    contenido = models.TextField(u'Contenido')
    publicado = models.BooleanField(u'Publicado', default=True)
    autor = models.ForeignKey(User)
    tag = models.ManyToManyField('Categoria')
    
    def __str__(self):
        return self.titulo

    
class Categoria(models.Model):
    nombre = models.CharField("Titulo de la Categoria", max_length=50)

    def __str__(self):
        return self.nombre
    
class Comentario(models.Model):
    class Meta:
        ordering=['-fecha']
    post = models.ForeignKey(Entrada)
    nick = models.CharField("publicado por:", max_length=50)
    contenido = models.TextField("Ahi lo anoto", max_length=500)
    fecha = models.DateTimeField("Fecha", auto_now_add=True)
        
    def __str__(self):
        return self.nick