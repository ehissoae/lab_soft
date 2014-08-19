from django.db import models
from django.template import Context
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from missoes.models import AlocacaoRecurso

class Recurso(models.Model):
  RESOURCES_TYPES = (("externo", "Externo"), ("internoFisico", "Interno Fisico"), ("internoHumano", "Interno Humano"))
  RESOURCES_STATUSES = (("ativo", "Ativo"), ("removido", "Removido"))
  nome = models.CharField(max_length=50)
  tipoRecurso = models.CharField(max_length=50,
                  choices=RESOURCES_TYPES)
  status = models.CharField(max_length=10,
                choices=RESOURCES_STATUSES,
                default="ativo")
  telefone = models.CharField(max_length=20)
  quantidadeTotal = models.IntegerField(null=True, blank=True)
  descricao = models.CharField(max_length=200)

  def quantidadeDisponivel(self):
    alocados = AlocacaoRecurso.objects.filter(recurso_id=self.id)
    quantidadeAlocada = 0
    if alocados.count() > 0:
      for alocado in alocados:
        qtd = alocado.quantidadeAlocada
        if qtd > 0 and (alocado.missao.status not in ['removido', 'finalizadoComSucesso', 'finalizadoSemSucesso']):
          quantidadeAlocada += qtd
    return self.quantidadeTotal - quantidadeAlocada

  def __unicode__(self):
    return self.get_tipoRecurso_display() + " - " + self.nome

  def get_absolute_url(self):
    return "/recursos/detalhes?id=" + str(self.id)