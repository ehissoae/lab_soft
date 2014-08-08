from django.conf.urls import url

from missoes import views

urlpatterns = [
    url(r'^$', views.index, name='missoes'),
    url(r'^detalhes$', views.detail, name='detalhes'),
    url(r'^novo$', views.new, name='novo'),
    url(r'^alterarStatus$', views.changeStatus, name='alterar_status'),
    url(r'^alocarRecurso$', views.assignResource, name='alocar_recurso'),
    url(r'^detalhesRecursoAlocado$', views.assignedResourceDetails, name='detalhes_recurso_alocado'),
    url(r'^removerRecursoAlocado$', views.deleteAssignedResource, name='remover_recurso_alocado'),
    url(r'^remover$', views.delete, name='remover'),
]