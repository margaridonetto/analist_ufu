from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('new/', views.PostCreate.as_view(), name='new'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='detail'),
    path('<slug:slug>/edit/', views.PostUpdate.as_view(), name='edit'),
    path('<slug:slug>/delete/', views.PostDelete.as_view(), name='delete'),
]