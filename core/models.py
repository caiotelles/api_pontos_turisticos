from django.db import models
from atracoes.models import Recurso
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    aprovado = models.BooleanField(default=False)
    recursos = models.ManyToManyField(Recurso)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)

    def __str__(self):
        return self.nome
