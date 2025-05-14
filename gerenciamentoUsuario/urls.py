from django.urls import path, include
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from .views import StatusUsuarioViewSet, CadastrarUsuarioViewSet
from django.shortcuts import render
from .models import CadastroUsuario
from .models.cadastro import *
from .forms import CadastroUsuarioForm

app_name = 'gerenciamentoUsuario'

routher = DefaultRouter()
routher.register('Status', StatusUsuarioViewSet)
routher.register('Novo Usuario', CadastrarUsuarioViewSet)

def home_user_view(request):
    return render(request, 'gerenciamentoUsuario/home.html')

def usuarioList(request):
    usuarios = CadastroUsuario.objects.all()
    return render(request, 'gerenciamentoUsuario/lista.html', {'usuarios': usuarios})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            cpf = form.cleaned_data['cpf']
            status = form.cleaned_data['status']
            tipo_usuario = form.cleaned_data['tipo_usuario']

            if tipo_usuario == 'comum':
                criador = CriadorUsuarioComum()
            else:
                criador = CriadorUsuarioAdministrador()

            criador.operacao_cadastro(nome, email, cpf, status)

            return render(request, 'gerenciamentoUsuario/sucesso.html', {'nome': nome})
    else:
        form = CadastroUsuarioForm()

    return render(request, 'gerenciamentoUsuario/cadastro.html', {'form': form})

urlpatterns = [
    path('', home_user_view, name= "home"),
    path('usuarioList/', usuarioList, name= "usuarioList"),
    path('usuarioCadastro/', cadastrar_usuario, name= "usuarioCadastro")
    #path('', include(routher.urls)),
]
