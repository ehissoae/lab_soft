from django.conf.urls import url

from missoes import views

urlpatterns = [
    url(r'^$', views.index, name='missoes'),
    url(r'^detalhes$', views.detail, name='missaoDetalhes'),
    url(r'^novo$', views.new, name='missaoNovo'),
    url(r'^alterarStatus$', views.changeStatus, name='missaoAlterarStatus'),
    url(r'^alocarRecurso$', views.assignResource, name='missaoAlocarRecurso'),
    url(r'^detalhesRecursoAlocado$', views.assignedResourceDetails, name='missaoDetalhesRecursoAlocado'),
    url(r'^removerRecursoAlocado$', views.deleteAssignedResource, name='missaoRemoverRecursoAlocado'),
    url(r'^remover$', views.delete, name='missaoRemover'),
]