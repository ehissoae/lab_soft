from django.db import models
import datetime

class Missao(models.Model):
  nome = models.CharField(max_length=50)
  tipoMissao = models.CharField(max_length=20)
  status = models.CharField(max_length=20, default='aguardandoRecursos')
  acidente = models.ForeignKey("acidentes.Acidente") 
  recursos = models.ManyToManyField("recursos.Recurso", through='AlocacaoRecurso')

  def __unicode__(self):
    return self.nome

class AlocacaoRecurso(models.Model):
  recurso = models.ForeignKey("recursos.Recurso")
  missao = models.ForeignKey("missoes.Missao")
  quantidadeAlocada = models.IntegerField(null=True, blank=True)
  dataAlocacao = models.DateField(default=datetime.date.today)
  observacao = models.CharField(max_length=200)
