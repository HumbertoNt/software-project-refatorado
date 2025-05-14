from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LivroViewSet, StatusLivroViewSet
from django.shortcuts import render
from .models import Livro
from django.db.models import Q

app_name = 'gerenciamentoLivro'

routher = DefaultRouter()
routher.register('Livros', LivroViewSet)
routher.register('Status', StatusLivroViewSet)

def home_book_view(request):
    return render(request, 'gerenciamentoLivro/home.html')

def lista_livros(request):
    busca = request.GET.get('q', '')
    if busca:
        livros = Livro.objects.filter(
            Q(titulo__icontains=busca) | Q(autor__icontains=busca)
        )
    else:
        livros = Livro.objects.all()
    
    return render(request, 'gerenciamentoLivro/lista.html', {
        'livros': livros,
        'busca': busca
    })



urlpatterns = [
    path('', home_book_view, name= "home"),
    path('listaLivros/', lista_livros, name= "listaLivros"),
]
