import os
import django


# Configura o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistemaDeBiblioteca.settings')
django.setup()

from gerenciamentoLivro.models import Livro, StatusLivro
from gerenciamentoUsuario.models import CadastroUsuario, StatusUsuario
from abc import ABC, abstractmethod

class Usuario(ABC):
    @abstractmethod
    def cadastrar(self, nome, email, cpf, status):
        pass

class UsuarioComum(Usuario):
    def cadastrar(self, nome, email, cpf, status):
        novo_usuario = CadastroUsuario(
            nome=nome,
            email=email,
            cpf=cpf,
            status=status,
            usuario_comum=True,
            usuario_adm=False
        )
        novo_usuario.save()
        print(f"Usuário COMUM '{nome}' cadastrado com sucesso!")

class UsuarioAdministrador(Usuario):
    def cadastrar(self, nome, email, cpf, status):
        novo_usuario = CadastroUsuario(
            nome=nome,
            email=email,
            cpf=cpf,
            status=status,
            usuario_comum=False,
            usuario_adm=True
        )
        novo_usuario.save()
        print(f"Usuário ADMINISTRADOR '{nome}' cadastrado com sucesso!")


class CriadorUsuario(ABC):
    @abstractmethod
    def factory_method(self) -> Usuario:
        pass

    def operacao_cadastro(self, nome, email, cpf, status):
        usuario = self.factory_method()
        usuario.cadastrar(nome, email, cpf, status)

class CriadorUsuarioComum(CriadorUsuario):
    def factory_method(self) -> Usuario:
        return UsuarioComum()


class CriadorUsuarioAdministrador(CriadorUsuario):
    def factory_method(self) -> Usuario:
        return UsuarioAdministrador()

def cadastrar_usuario():
    nome = input("Nome: ")
    email = input("Email: ")
    cpf = input("CPF (somente números): ")

    print("Tipo de usuário:")
    print("1. Comum")
    print("2. Administrador")
    tipo_opcao = input("Escolha (1 ou 2): ")

    if tipo_opcao == "1":
        criador = CriadorUsuarioComum()
    elif tipo_opcao == "2":
        criador = CriadorUsuarioAdministrador()
    else:
        print("Tipo de usuário inválido.")
        return

    print("Escolha o status:")
    print("1. Ativo\n2. Inativo\n3. Bloqueado\n4. Suspenso")
    status_opcao = input("Escolha (1 a 4): ")

    status_dict = {
        "1": "Ativo",
        "2": "Inativo",
        "3": "Bloqueado",
        "4": "Suspenso"
    }

    status_nome = status_dict.get(status_opcao)
    if not status_nome:
        print("Opção de status inválida.")
        return

    try:
        status = StatusUsuario.objects.get(status=status_nome)
    except StatusUsuario.DoesNotExist:
        print(f"Status '{status_nome}' ainda não está cadastrado no banco.")
        return

    criador.operacao_cadastro(nome, email, cpf, status)


def listar_usuarios():
    usuarios = CadastroUsuario.objects.all()
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    print("Lista de usuários:")
    for u in usuarios:
        tipo = "Administrador" if u.usuario_adm else "Comum" if u.usuario_comum else "Desconhecido"
        print(f"[{u.id}] {u.nome} | Email: {u.email} | CPF: {u.cpf} | Tipo: {tipo} | Status: {u.status}")

def adicionar_livro(titulo, autor):
    status_padrao = StatusLivro.objects.first()  # ou filtre por nome
    if not status_padrao:
        return

    novo_livro = Livro(titulo=titulo, autor=autor, statusLivro=status_padrao)
    novo_livro.save()

def listar_livros():
    livros = Livro.objects.all()
    if livros.exists():
        print("Livros cadastrados:")
        for livro in livros:
            print(f"- {livro.titulo} (Autor: {livro.autor})")
    else:
        print("Nenhum livro cadastrado.")

def main():
    while True:
        print("\n=== MENU ===")
        print("1. Listar livros")
        print("2. Adicionar livro")
        print("3. Listar usuarios")
        print("2. Adicionar usuario")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            listar_livros()
        elif escolha == '2':
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            adicionar_livro(titulo, autor)
        elif escolha == '3':
            listar_usuarios()
        elif escolha == '4':
            cadastrar_usuario()
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == '__main__':
    main()
