from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('new/', views.PostCreate.as_view(), name='new'),
    path('clientes/', views.Clientes.as_view(), name='clientes'),
    path('fornecedores/', views.Fornecedores.as_view(), name='fornecedores'),
    path('produtos/', views.Produtos.as_view(), name='produtos'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='detail'),
    path('<slug:slug>/edit/', views.PostUpdate.as_view(), name='edit'),
    path('<slug:slug>/delete/', views.PostDelete.as_view(), name='delete'),
    path('calor/', views.MapaCalor.as_view(), name='mapaCalor'),
]