from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class Recurso(models.Model):
  tipoRecurso = models.CharField(max_length=50)
  nome = models.CharField(max_length=50)
  status = models.CharField(max_length=10)
  phoneNumber = models.CharField(max_length=20)

  def __unicode__(self):
    return self.nome