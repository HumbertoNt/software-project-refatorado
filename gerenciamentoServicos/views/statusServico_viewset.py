from rest_framework.viewsets import ModelViewSet
from ..serializers import EventoSerializer
from ..models import Evento

class EventoViewSet(ModelViewSet):
    queryset = Evento.objects.all() 
    serializer_class = EventoSerializer