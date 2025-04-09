from rest_framework.viewsets import ModelViewSet
from ..serializers import LivroSerializer
from ..models import Livro

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()  
    serializer_class = LivroSerializer