from rest_framework.viewsets import ModelViewSet
from ..serializers import CadastrarUsuarioSerializer
from ..models import CadastroUsuario

class CadastrarUsuarioViewSet(ModelViewSet):
    queryset = CadastroUsuario.objects.all()
    serializer_class = CadastrarUsuarioSerializer