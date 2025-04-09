from rest_framework import serializers
from ..models import Evento, StatusServico

class StatusServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusServico
        fields = ['statusEvento']

class EventoSerializer(serializers.ModelSerializer):
    statusServico = StatusServicoSerializer(read_only=True)
    statusServico_id = serializers.PrimaryKeyRelatedField(
        queryset=StatusServico.objects.all(), 
        source='statusServico', 
        write_only=True
    )  

    class Meta:
        model = Evento
        fields = [
            'nome',
            'data',
            'horario',
            'local',
            'statusServico', 
            'statusServico_id' 
        ]
