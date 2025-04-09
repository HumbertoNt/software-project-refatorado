from rest_framework.viewsets import ModelViewSet
from ..serializers import StatusServicoSerializer
from ..models import StatusServico

class StatusEventoViewSet(ModelViewSet):
    queryset = StatusServico.objects.all()
    serializer_class = StatusServicoSerializer
    
