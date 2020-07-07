from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
   STATUS = (
      ('rascunho','Rascunho'),
      ('publicado', 'Publicado'),
   )
   titulo = models.CharField(max_length=100)
   slug = models.SlugField(max_length=250)
   autor = models.ForeignKey(User,on_delete=models.CASCADE)
   conteudo = models.TextField()
   publicado = models.DateTimeField(default=timezone.now())
   criado = models.DateTimeField(auto_now_add=True)
   editado = models.DateTimeField(auto_now=True)
   status = models.CharField(max_length=10,choices=STATUS,default='rascunho')


   class Meta:
      ordering = ('-publicado',)

   def __str__(self):
      return self.titulo