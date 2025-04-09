from django.db import models
from .statusServico import *

from django.db import models
from .statusServico import *

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField(null=True, blank=True)
    horario = models.TimeField(null=True, blank=True)
    local = models.CharField(max_length=100)
    statusServico = models.ForeignKey('StatusServico', on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'Evento'
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        
    def __str__(self):
        return self.nome