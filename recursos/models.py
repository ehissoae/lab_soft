from django.db import models

class Recurso(models.Model):
  tipo_recurso = models.CharField(max_length=50)
  nome = models.CharField(max_length=50)
  status = models.CharField(max_length=10)
  phone_number = models.CharField(max_length=20)

  def __unicode__(self):
    return self.nome