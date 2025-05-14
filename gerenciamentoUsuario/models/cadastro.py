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
