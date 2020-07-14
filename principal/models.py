from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save

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

   def get_absolut_url(self):
      return reverse('detail', args=[self.slug])

   class Meta:
      ordering = ('-publicado',)

   def __str__(self):
      return self.titulo

@receiver(post_save,sender= Post)
def insert_slug(sender, instance,**kwargs):
   if not instance.slug:
      instance.slug = slugify(instance.titulo)
      return instance.save()