from django.db import models
from django.template import Context
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class Recurso(models.Model):
  RESOURCES_TYPES = (("externo", "Externo"), ("internoFisico", "Interno Fisico"), ("internoHumano", "Interno Humano"))
  RESOURCES_STATUSES = (("ativo", "ativo"), ("removido", "removido"))
  nome = models.CharField(max_length=50)
  tipoRecurso = models.CharField(max_length=50,
  								choices=RESOURCES_TYPES)
  status = models.CharField(max_length=10,
  							choices=RESOURCES_STATUSES,
  							default="ativo")
  telefone = models.CharField(max_length=20)
  quantidadeTotal = models.IntegerField(null=True, blank=True)
  descricao = models.CharField(max_length=200)

  def __unicode__(self):
    return self.tipoRecurso + " - " + self.nome
