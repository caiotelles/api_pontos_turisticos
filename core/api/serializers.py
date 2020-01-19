from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer

class PontoTuristicoSerializer(ModelSerializer):

    recursos = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    endereco = EnderecoSerializer()
    avaliacoes = AvaliacaoSerializer(many=True)
    descricao_completa = SerializerMethodField()


    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
                  'recursos', 'comentarios', 'avaliacoes',
                  'endereco', 'descricao_completa', 'descricao_completa2'
                  )

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
