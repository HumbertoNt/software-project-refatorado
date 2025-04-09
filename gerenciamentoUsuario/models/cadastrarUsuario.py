from django.db import models 
from .statusUsuario import *     

class CadastroUsuario(models.Model):
    
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    status = models.ForeignKey('StatusUsuario', on_delete=models.DO_NOTHING)
    usuario_comum = models.BooleanField(default=False)
    usuario_adm = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'CadastroUsuario'
        verbose_name = 'CadastroUsuario'
        verbose_name_plural = 'CadastroUsuarios'
        
    def __str__(self):
        return self.nome
    
    def __srt__(self):
        return self.status 
