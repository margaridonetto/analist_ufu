from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Post
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'principal/home.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'principal/detail.html'
    context_object_name = 'customizado'
