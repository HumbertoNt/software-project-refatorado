from rest_framework.viewsets import ModelViewSet
from ..serializers import StatusUsuarioSerializer
from ..models import StatusUsuario

class StatusUsuarioViewSet(ModelViewSet):
    queryset = StatusUsuario.objects.all()
    serializer_class = StatusUsuarioSerializer