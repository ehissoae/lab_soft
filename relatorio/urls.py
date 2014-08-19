from django.conf.urls import url
from relatorio import views

urlpatterns = [
  url(r'^$', views.relatorio, name='relatorio'),
  url(r'^gerarRelatorio$', views.gerarRelatorio, name='gerarRelatorio')
]