from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from . models import Post
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
    fields = ('autor','titulo','conteudo')

class PostUpdate(UpdateView):
    model = Post
    template_name = 'principal/edit.html'
    fields = ('titulo','conteudo')

class PostDelete(DeleteView):
    model = Post
    template_name = 'principal/delete.html'
    success_url = reverse_lazy("home")

