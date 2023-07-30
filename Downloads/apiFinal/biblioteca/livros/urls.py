from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('editar/<str:id>/', views.editar, name='editar'),
    path('deletar/<str:id>/', views.deletar, name='deletar'),
]
