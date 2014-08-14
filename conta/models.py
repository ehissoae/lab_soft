from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
  ROLE_CHOICES = (
    ("administrador", 'Administrador'),
    ("coordenador", 'Coordenador'),
    ("especialista", 'Especialista'),
  )
  user = models.OneToOneField(User)
  tipoAcesso = models.CharField(max_length=100,
                                choices=ROLE_CHOICES, 
                                default="coordenador")

  def get_absolute_url(self):
    return "/conta/detalhes?id=" + str(self.user.id)