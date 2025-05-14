from django import forms
from .models import StatusUsuario

class CadastroUsuarioForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    cpf = forms.CharField(max_length=11)
    status = forms.ModelChoiceField(queryset=StatusUsuario.objects.all(), empty_label="Selecione o status")
    
    TIPO_USUARIO_CHOICES = [
        ('comum', 'Usuário Comum'),
        ('adm', 'Usuário Administrador')
    ]
    tipo_usuario = forms.ChoiceField(choices=TIPO_USUARIO_CHOICES)
