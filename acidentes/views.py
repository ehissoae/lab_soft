# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from acidentes.models import Acidente
from datetime import datetime
from django.contrib import messages
from SiGeCAV.utils import *

# Create your views here.
def index(request):
  url = url_if_not_authenticated(request)
  if(url):
    return url

  acidentes = Acidente.objects.exclude(status="removido")
  return render(request, 'acidentes/index.html', {'acidentes': acidentes})

def detail(request):
  url = url_if_not_authenticated(request)
  if(url):
    return url
  acidenteId = request.GET.get("id", "")
  acidente = Acidente.objects.get(id=acidenteId)
  missoes = acidente.missao_set.exclude(status="removido").all()
  return render(request, 'acidentes/detalhes.html', {
    'acidente': acidente,
    'missoes': missoes,
  })

def new(request):
  url = url_if_not_coordenador(request)
  if(url):
    return url

  if request.method == "GET":
    return render(request, 'acidentes/novo.html', {})
  elif request.method == "POST":
    dataHora = request.POST.get("dataHora", "")
    local = request.POST.get("local", "")
    descricao = request.POST.get("descricao", "")
    SVCid = request.POST.get("SVCid", "")
    if not "http://" in SVCid:
      SVCid = "http://" + SVCid
    if dataHora and local and descricao:
      dataHoraFormatada = datetime.strptime(dataHora, '%d/%m/%Y %H:%M')
      num_results = Acidente.objects.filter(dataHora=dataHoraFormatada, local=local, SVCid=SVCid, descricao=descricao).exclude(status="removido").count()
      if num_results == 0:
        acidente = Acidente.objects.create(coordenador=request.user, dataHora=dataHoraFormatada, local=local, SVCid=SVCid, descricao=descricao)
        return redirect(acidente)
      else:
        messages.error(request, 'Acidente já existe.')
    return render(request, 'acidentes/novo.html', {'dataHora': dataHora, 'local': local, 'descricao': descricao, 'SVCid': SVCid})

def edit(request):
  url = url_if_not_coordenador(request)
  if(url):
    return url

  if request.method == "GET":
    acidenteId = request.GET.get("id", "")
    acidente = Acidente.objects.get(id=acidenteId)
    return render(request, 'acidentes/editar.html', {'acidente': acidente})
  elif request.method == "POST":
    acidenteId = request.POST.get("id", "")
    acidente = Acidente.objects.get(id=acidenteId)
    dataHora = request.POST.get("dataHora", "")
    dataHora = datetime.strptime(dataHora, '%d/%m/%Y %H:%M')
    acidente.dataHora = dataHora
    acidente.local = request.POST.get("local", "")
    acidente.descricao = request.POST.get("descricao", "")
    acidente.SVCid = request.POST.get("SVCid", "")
    acidente.save()
    return redirect(acidente)

def delete(request):
  url = url_if_not_administrador(request)
  if(url):
    return url

  acidenteId = request.GET.get("id", "")
  acidente = Acidente.objects.get(id=acidenteId)
  acidente.status = "removido"
  for missao in acidente.missao_set.exclude(status="removido"):
    missao.status = "removido"
    missao.save()
  acidente.save()
  return redirect('acidentes')
