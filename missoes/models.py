from django.db import models
from acidentes.models import Acidente 

class Missao(models.Model):
  nome = models.CharField(max_length=50)
  tipoMissao = models.CharField(max_length=20)
  status = models.CharField(max_length=20, default='aguardandoRecursos')
  acidente = models.ForeignKey(Acidente) 

  def __unicode__(self):
    return self.nome