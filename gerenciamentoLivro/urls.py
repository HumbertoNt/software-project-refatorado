from django.urls import path, include
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from .views import LivroViewSet, StatusLivroViewSet
from django.shortcuts import render
from .models.livro import *
from .models import StatusLivro
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

def mudar_status_livro(request, livro_id, novo_status):

    livro = get_object_or_404(Livro, pk=livro_id)

    if novo_status in dict(StatusLivro.STATUS_CHOICES).keys():

        observer = ConcreteObserver()
        livro.attach(observer)

        livro.change_status(novo_status)

        livro.detach(observer)

        return redirect('gerenciamentoLivro:listaLivros')
    else:
        return render(request, 'gerenciamentoLivro/erro.html', {
            'mensagem': 'Status inválido.'
        })


urlpatterns = [
    path('', home_book_view, name= "home"),
    path('listaLivros/', lista_livros, name= "listaLivros"),
    path('mudarStatus/<int:livro_id>/<str:novo_status>/', mudar_status_livro, name="mudarStatus"),
]
