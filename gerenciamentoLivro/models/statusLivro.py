from django.db import models

class StatusLivro(models.Model):
    STATUS_CHOICES = [
        ('Disponivel', 'Disponível'),
        ('Alugado', 'Alugado'),
        ('Reservado', 'Reservado'),
        ('Alugado e reservado', 'Alugado e Reservado'),
    ]
    
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='disponivel')

    def __str__(self):
        return self.get_status_display()