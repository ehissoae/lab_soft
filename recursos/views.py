from django.shortcuts import render
from recursos.models import Recurso
from SiGeCAV.utils import *

# Create your views here.
def index(request):
  url = url_if_not_authenticated(request)
  if(url):
    return url
  recursos = Recurso.objects.all()
  tipoAcesso = request.user.profile.tipoAcesso
  return render(request, 'recursos/index.html', {"tipoAcesso":tipoAcesso, 'recursos': recursos})

def detail(request):
  recursoId = request.GET.get("id", "")
  recurso = Recurso.objects.get(id=recursoId)
  return render(request, 'recursos/detalhes.html', {'recurso': recurso})

def new(request):
  if request.method == "GET":
    return render(request, 'recursos/novo.html', {})
  elif request.method == "POST":
    tipoRecurso = request.POST.get("tipoRecurso", "")
    nome = request.POST.get("nome", "")
    telefone = request.POST.get("telefone", "")

    if tipoRecurso and nome and telefone:
      Recurso.objects.create(tipoRecurso=tipoRecurso, nome=nome, telefone=telefone)
      return index(request)
    return render(request, 'recursos/novo.html', {})

def edit(request):
  if request.method == "GET":
    recursoId = request.GET.get("id", "")
    recurso = Recurso.objects.get(id=recursoId)
    return render(request, 'recursos/editar.html', {'recurso': recurso})
  elif request.method == "POST":
    recursoId = request.POST.get("id", "")
    recurso = Recurso.objects.get(id=recursoId)
    
    recurso.tipoRecurso = request.POST.get("tipoRecurso", "")
    recurso.nome = request.POST.get("nome", "")
    recurso.status = request.POST.get("status", "")
    recurso.telefone = request.POST.get("telefone", "")
    recurso.save()
    return render(request, 'recursos/detalhes.html', {'recurso': recurso})

def delete(request):
  recursoId = request.GET.get("id", "")
  Recurso.objects.get(id=recursoId).delete()
  return index(request)