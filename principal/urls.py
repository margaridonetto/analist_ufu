from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='detail'),
]