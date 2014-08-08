from django.conf.urls import url

from conta import views

urlpatterns = [
  url(r'^login$', views.custom_login, name="custom_login"),
  url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/conta/login'}),
  
  url(r'^$', views.index, name='usuarios'),
  url(r'^detalhes$', views.detail, name='usuarioDetalhes'),
  url(r'^novo$', views.new, name='usuarioNovo'),
  url(r'^editar$', views.edit, name='usuarioEditar'),
  url(r'^remover$', views.delete, name='usuarioRemover'),
  ]