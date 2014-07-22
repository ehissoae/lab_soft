from django.db import models

from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User)
    tipoAcesso = models.CharField(max_length=100)

