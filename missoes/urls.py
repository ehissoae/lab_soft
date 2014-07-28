from django.conf.urls import url

from missoes import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detalhes$', views.detail, name='detalhes'),
    url(r'^novo$', views.new, name='novo'),
    url(r'^alterarStatus$', views.changeStatus, name='alterar_status'),
    url(r'^remover$', views.delete, name='remover'),
]