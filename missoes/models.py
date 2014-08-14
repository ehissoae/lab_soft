# -*- coding: utf-8 -*-

from django.db import models
import datetime

class Missao(models.Model):
  STATUSES_TYPES = (
    ("aguardandoRecursos", 'Aguardando Alocação de Recursos'),
    ("finalizadoComSucesso", 'Finalizado com Sucesso'),
    ("finalizadoSemSucesso", 'Finalizado sem Sucesso'),
    ("emAndamento", 'Em Andamento'),
    ("removido", 'Removido'),
  )
  MISSION_TYPES = (
    ("resgate", "Resgate"),
    ("remocaoObstaculo", "Remoção de Obstáculos"),
    ("transporte", "transporte"),
    ("socorroVitima", "Socorros à Vítima"),
    ("remocaoVitima", "Remoção da Vítima"),
  )
  nome = models.CharField(max_length=50)
  tipoMissao = models.CharField(max_length=20, choices=MISSION_TYPES)
  status = models.CharField(max_length=20, default='aguardandoRecursos', choices=STATUSES_TYPES)
  acidente = models.ForeignKey("acidentes.Acidente") 
  recursos = models.ManyToManyField("recursos.Recurso", through='AlocacaoRecurso')

  def __unicode__(self):
    return self.nome

class AlocacaoRecurso(models.Model):
  recurso = models.ForeignKey("recursos.Recurso")
  missao = models.ForeignKey("missoes.Missao")
  quantidadeAlocada = models.IntegerField(null=True, blank=True)
  dataAlocacao = models.DateField(default=datetime.date.today)
  observacao = models.CharField(max_length=200)
