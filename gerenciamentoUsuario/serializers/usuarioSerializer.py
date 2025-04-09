from rest_framework import serializers
from ..models import CadastroUsuario, StatusUsuario

class StatusUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusUsuario
        fields = [
            'status'
        ]
        
class CadastrarUsuarioSerializer(serializers.ModelSerializer):
    status_info = serializers.SerializerMethodField()
    
    class Meta:
        model = CadastroUsuario
        fields = [
            'nome',
            'email',
            'cpf',
            'status',
            'usuario_comum',
            'usuario_adm',
            'status_info'
        ]
        
    def get_status_info(self, obj):
        return obj.status.status
    