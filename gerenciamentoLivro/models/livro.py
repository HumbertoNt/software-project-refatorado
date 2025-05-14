from .statusLivro import *
from django.db import models
from abc import ABC, abstractmethod
from abc import ABC, abstractmethod

class Subject(ABC):
    """
    A classe Subject para gerenciar os observadores.
    """

    @abstractmethod
    def attach(self, observer: "Observer") -> None:
        pass

    @abstractmethod
    def detach(self, observer: "Observer") -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField(null=True, blank=True)
    edicao = models.IntegerField(null=True, blank=True)
    statusLivro = models.ForeignKey('StatusLivro', on_delete=models.DO_NOTHING)

    _observers = []

    class Meta:
        db_table = 'Livro'
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.titulo

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def change_status(self, new_status: str) -> None:
        """
        Altera o status do livro e notifica os observadores.
        """
        if self.statusLivro.status != new_status:
            try:
                status_obj = StatusLivro.objects.get(status=new_status)
                self.statusLivro = status_obj
                self.save()
                self.notify() 
            except StatusLivro.DoesNotExist:
                print(f"Erro: Status '{new_status}' não encontrado.")

class ConcreteObserver(Observer):
    def update(self, subject: Subject) -> None:
        if isinstance(subject, Livro):
            print(f"Livro '{subject.titulo}' agora está com o status '{subject.statusLivro.status}'.")
