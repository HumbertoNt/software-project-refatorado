from rest_framework.viewsets import ModelViewSet
from ..serializers import StatusLivroSerializer
from ..models import StatusLivro

#class herdando de ModelViewSet para 'gerenciar' o modelo StatusLivro
class StatusLivroViewSet(ModelViewSet):
    queryset = StatusLivro.objects.all()
    serializer_class = StatusLivroSerializer
