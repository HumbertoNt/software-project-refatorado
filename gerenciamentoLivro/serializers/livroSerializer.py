from rest_framework import serializers
from ..models import Livro, StatusLivro

class StatusLivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusLivro
        fields = [
            'status'
        ]
        
class LivroSerializer(serializers.ModelSerializer):
    statusLivro = serializers.SerializerMethodField(read_only=True)
    statusLivro_id = serializers.PrimaryKeyRelatedField(
        queryset=StatusLivro.objects.all(), 
        source='statusLivro', 
        write_only=True
    )
    
    class Meta:
        model = Livro
        fields = [
            'titulo',
            'autor',
            'ano',
            'edicao',
            'statusLivro',
            'statusLivro_id'
        ]
        
    def get_statusLivro(self, obj):
        return obj.statusLivro.status
    
    def get_livro(self, obj):
        return obj.livro.titulo
    
    def get_livro(self, obj):
        return obj.livro.autor
