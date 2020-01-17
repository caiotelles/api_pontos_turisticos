from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
        serializer_class = PontoTuristicoSerializer
        filter_backends = [SearchFilter]
        search_fields = ['nome', 'descricao', 'endereco__linha1']

        def get_queryset(self):
            id = self.request.query_params.get('id', None)
            nome = self.request.query_params.get('nome', None)
            descricao = self.request.query_params.get('descricao', None)
            queryset = PontoTuristico.objects.all()
            if id:
                queryset = PontoTuristico.objects.filter(pk=id)

            if nome:
                queryset = queryset.filter(nome__iexact=nome)

            if descricao:
                queryset = queryset.filter(descricao__iexact=descricao)

            return queryset
            #return PontoTuristico.objects.filter(aprovado=True)

#       def get_queryset(self):
#           return PontoTuristico.objects.filter(aprovado=True)

#       def list(self, request, *args, **kwargs):
#           return Response({'teste': 123})

#       def create(self, request, *args, **kwargs):
#           return Response({'Hello': request.data['nome']})

#       def destroy(self, request, *args, **kwargs):
#           pass

#       def retrieve(self, request, *args, **kwargs):
#           pass

#       def update(self, request, *args, **kwargs):
#           pass

#       def partial_update(self, request, *args, **kwargs):
#           pass

        @action(methods=['GET', 'POST'], detail=True)
        def denunciar(self, request, pk=None):
            pass

        @action(methods=['GET'], detail=False)
        def teste(self, request):
            pass