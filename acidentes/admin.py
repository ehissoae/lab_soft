from django.contrib import admin
from acidentes.models import Acidente

class AcidenteAdmin(admin.ModelAdmin):
  exclude = ("dataHora", "local", "descricao", "SVCid", "status", "coordenador", "especialista")

admin.site.register(Acidente, AcidenteAdmin)
