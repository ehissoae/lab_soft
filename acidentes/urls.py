from django.conf.urls import url

from acidentes import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detalhes$', views.detail, name='detalhes'),
    url(r'^novo$', views.new, name='novo'),
    url(r'^editar$', views.edit, name='editar'),
    url(r'^remover$', views.delete, name='remover'),
]