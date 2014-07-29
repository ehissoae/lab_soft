from django.conf.urls import url

from acidentes import views

urlpatterns = [
    url(r'^$', views.index, name='acidentes'),
    url(r'^detalhes$', views.detail, name='acidenteDetalhes'),
    url(r'^novo$', views.new, name='acidenteNovo'),
    url(r'^editar$', views.edit, name='acidenteEditar'),
    url(r'^remover$', views.delete, name='acidenteRemover'),
]