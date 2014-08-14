from django.db import models
from django.contrib.auth.models import User 

class Acidente(models.Model):
  dataHora = models.DateTimeField()
  local = models.CharField(max_length=50)
  descricao = models.CharField(max_length=200)
  SVCid = models.CharField(max_length=50, null=True)
  status = models.CharField(max_length=20, default='aguardandoAnalise')
  coordenador = models.ForeignKey(User, related_name='acidentesCoordenador', null=True)
  especialista = models.ForeignKey(User, related_name='acidentesEspecialista', null=True) 

  def __unicode__(self):
    return self.local

  def get_absolute_url(self):
    return "/acidentes/detalhes?id=" + str(self.id)