from django.db import models

class StatusServico(models.Model):
    STATUS_CHOICES = [
        ('Agendado', 'Agendado'),
        ('Em andamento', 'Em andamento'),
        ('Cancelado', 'Cancelado'),
        ('Finalizado', 'Finalizado'),
    ]
    
    statusEvento = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Em andamento')
    
    def __str__(self):
        return self.get_status_display()