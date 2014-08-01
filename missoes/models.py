from django.db import models
from recursos.models import Recurso
from acidentes.models import Acidente 
import datetime

class Missao(models.Model):
  nome = models.CharField(max_length=50)
  tipoMissao = models.CharField(max_length=20)
  status = models.CharField(max_length=20, default='aguardandoRecursos')
  acidente = models.ForeignKey(Acidente) 
  recursos = models.ManyToManyField(Recurso, through='AlocacaoRecurso')

  def __unicode__(self):
    return self.nome

class AlocacaoRecurso(models.Model):
  recurso = models.ForeignKey(Recurso)
  missao = models.ForeignKey(Missao)
  quantidadeAlocada = models.IntegerField(default=0)
  dataAlocacao = models.DateField(default=datetime.date.today)