from rest_framework.viewsets import ModelViewSet
from atracoes.models import Recurso
from .serializers import AtracaoSerializer

class AtracoesViewSet(ModelViewSet):
    queryset = Recurso.objects.all()
    serializer_class = AtracaoSerializer