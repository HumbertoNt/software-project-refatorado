from django.db import models
from .statusLivro import *

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField(null=True, blank=True) #integerfield é um campo de número inteiro
    edicao = models.IntegerField(null=True, blank=True)
    statusLivro = models.ForeignKey('StatusLivro', on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'Livro'
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        
    def __str__(self):
        return self.titulo
