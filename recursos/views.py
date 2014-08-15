# -*- coding: utf-8 -*-

from django.shortcuts import render
from recursos.models import Recurso
from SiGeCAV.utils import *
from django.contrib import messages 

# Create your views here.
def index(request):
  recursos = Recurso.objects.exclude(status="removido")
  tipoAcesso = request.user.profile.tipoAcesso
  return render(request, 'recursos/index.html', {
    "tipoAcesso": tipoAcesso, 
    'recursos': recursos
    })

def detail(request):
  url = url_if_not_administrador(request)
  if(url):
    return url

  recursoId = request.GET.get("id", "")
  recurso = Recurso.objects.get(id=recursoId)
  return render(request, 'recursos/detalhes.html', {
    'recurso': recurso
    })

def new(request):
  url = url_if_not_administrador(request)
  if(url):
    return url

  if request.method == "GET":
    return render(request, 'recursos/novo.html', {
      'resources_types': Recurso.RESOURCES_TYPES,
      'resources_statuses': Recurso.RESOURCES_STATUSES,
      })
  elif request.method == "POST":
    nome = request.POST.get("nome", "")
    tipoRecurso = request.POST.get("tipoRecurso", "")
    telefone = request.POST.get("telefone", "")
    quantidadeTotal = request.POST.get("quantidadeTotal", 0)
    descricao = request.POST.get("descricao", "")

    if tipoRecurso and nome and telefone:
      num_results = Recurso.objects.filter(nome=nome, tipoRecurso=tipoRecurso).exclude(status="removido").count()
      if num_results == 0:
        Recurso.objects.create(nome=nome, tipoRecurso=tipoRecurso, telefone=telefone, quantidadeTotal=quantidadeTotal, descricao=descricao)
        return redirect(recurso)
      else:
        messages.error(request, 'Recurso já existe.')
    return render(request, 'recursos/novo.html', {
      'resources_types': Recurso.RESOURCES_TYPES,
      'resources_statuses': Recurso.RESOURCES_STATUSES,
      })

def edit(request):
  url = url_if_not_administrador(request)
  if(url):
    return url

  if request.method == "GET":
    recursoId = request.GET.get("id", "")
    recurso = Recurso.objects.get(id=recursoId)
    return render(request, 'recursos/editar.html', {
      'recurso': recurso,
      'resources_types': Recurso.RESOURCES_TYPES,
      'resources_statuses': Recurso.RESOURCES_STATUSES,
      })
  elif request.method == "POST":
    recursoId = request.POST.get("id", "")
    recurso = Recurso.objects.get(id=recursoId)
    
    recurso.nome = request.POST.get("nome", "")
    recurso.tipoRecurso = request.POST.get("tipoRecurso", "")
    recurso.status = request.POST.get("status", "")
    recurso.telefone = request.POST.get("telefone", "")
    recurso.quantidadeTotal = request.POST.get("quantidadeTotal", 0)
    recurso.descricao = request.POST.get("descricao", "")
    recurso.save()
    return redirect(recurso)

def delete(request):
  url = url_if_not_administrador(request)
  if(url):
    return url
  
  recursoId = request.GET.get("id", "")
  recurso = Recurso.objects.get(id=recursoId)
  recurso.status = "removido"
  recurso.save()
  return redirect('recursos')
