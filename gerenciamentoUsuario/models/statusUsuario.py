from django.db import models

class StatusUsuario(models.Model):
    STATUS_CHOICES = [
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
        ('Bloqueado', 'Bloqueado'),
        ('Suspenso', 'Suspenso'),
    ]
    
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Ativo')

    def __str__(self):
        return self.get_status_display()