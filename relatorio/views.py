# -*- coding: utf-8 -*-

from django.shortcuts import render
from acidentes.models import Acidente
from SiGeCAV.utils import *
from datetime import datetime

def relatorio(request):
  return render(request, 'relatorio/relatorio.html', {})

def gerarRelatorio(request):
  dataInicial = request.POST.get("dataInicial", "")
  dataFinal = request.POST.get("dataFinal", "")

  dataFinalCoxa = dataFinal + ' 23:59'

  if dataInicial and dataFinal:
    dataInicialFormatada = datetime.strptime(dataInicial, '%d/%m/%Y')
    dataFinalFormatada = datetime.strptime(dataFinalCoxa, '%d/%m/%Y %H:%M')

    acidentes = Acidente.objects.filter(dataHora__gte=dataInicialFormatada, dataHora__lte=dataFinalFormatada)

    return render(request, 'relatorio/gerarRelatorio.html', {
      'dataInicial': dataInicial, 
      'dataFinal': dataFinal,
      'acidentesAnalise': acidentes.filter(status='aguardandoAnalise'),
      'acidentesAndamento': acidentes.filter(status='emAndamento'),
      'acidentesFinalizados': acidentes.filter(status='finalizado'),
      'acidentesRemovidos': acidentes.filter(status='removido')
    })

  else:
    return render(request, 'relatorio/relatorio.html', {'dataInicial': dataInicial, 'dataFinal': dataFinal})