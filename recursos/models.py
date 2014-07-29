from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class Recurso(models.Model):
  tipoRecurso = models.CharField(max_length=50)
  nome = models.CharField(max_length=50)
  status = models.CharField(max_length=10,default="ativo")
  telefone = models.CharField(max_length=20)
  quantidadeTotal = models.IntegerField(default=1)

  def __unicode__(self):
    return self.tipoRecurso + " - " + self.nome
