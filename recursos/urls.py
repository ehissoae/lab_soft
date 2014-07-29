from django.conf.urls import url

from recursos import views

urlpatterns = [
  url(r'^$', views.index, name='recursos'),
  url(r'^novo$', views.new, name='recursoNovo'),
  url(r'^detalhes$', views.detail, name='recursoDetalhes'),
  url(r'^editar$', views.edit, name='recursoEditar'),
  url(r'^remover$', views.delete, name='recursoRemover'),
]