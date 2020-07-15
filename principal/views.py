from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Post, Clientes


# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'principal/home.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'principal/detail.html'
    context_object_name = 'customizado'

class PostCreate(CreateView):
    model = Post
    template_name = 'principal/newpost.html'
    fields = {'titulo','conteudo','autor','status'}
    success_message = "%(field)s criado com sucesso!!"
    success_url = reverse_lazy("home")

class PostUpdate(UpdateView):
    model = Post
    template_name = 'principal/edit.html'
    fields = ('titulo','conteudo','status')
    success_message = "%(field)s alterado com sucesso!!"
    success_url = reverse_lazy("home")


class PostDelete(DeleteView):
    model = Post
    template_name = 'principal/delete.html'
    success_url = reverse_lazy("home")

class Clientes(CreateView):
    model = Post
    template_name = 'principal/clientes.html'
    fields = ('__all__')

class Fornecedores(CreateView):
    model = Post
    template_name = 'principal/fornecedores.html'
    fields = ('__all__')

class Produtos(CreateView):
    model = Post
    template_name = 'principal/produtos.html'
    fields = ('__all__')

class MapaCalor(CreateView):
    model = Post
    template_name = 'principal/mapa_clientes.html'