from django.shortcuts import render
from missoes.models import Missao
from acidentes.models import Acidente

# Create your views here.
def index(request):
  acidenteId = request.GET.get("acidente_id", "")
  acidente = Acidente.objects.get(id=acidenteId)
  missoes = acidente.missao_set.all()
  return render(request, 'missoes/index.html', {'acidente': acidente, 'missoes': missoes})

def detail(request):
  missaoId = request.GET.get("id", "")
  missao = Missao.objects.get(id=missaoId)
  return render(request, 'missoes/detalhes.html', {'missao': missao})

def new(request):
  if request.method == "GET":
    acidenteId = request.GET.get("acidente_id", "")
    acidente = Acidente.objects.get(id=acidenteId)
    return render(request, 'missoes/novo.html', {'acidente':acidente})
  elif request.method == "POST":
    nome = request.POST.get("nome", "")
    tipoMissao = request.POST.get("tipoMissao", "")
    acidenteId = request.POST.get("acidente_id", "")
    if nome and tipoMissao and acidenteId:
      Missao.objects.create(nome=nome, tipoMissao=tipoMissao, acidente_id=acidenteId)
      return index2(request, acidenteId)
    return render(request, 'missoes/novo.html', {})

def changeStatus(request):
  if request.method == "GET":
    missaoId = request.GET.get("id", "")
    missao = Missao.objects.get(id=missaoId)
    return render(request, 'missoes/alterarStatus.html', {'missao': missao})
  elif request.method == "POST":
    missaoId = request.GET.get("id", "")
    missao = Missao.objects.get(id=missaoId)
    missao.status = request.POST.get("status", "")
    missao.save()
    return render(request, 'missoes/detalhes.html', {'missao': missao})

def delete(request):
  missaoId = request.GET.get("id", "")
  missao = Missao.objects.get(id=missaoId)
  acidenteId = missao.acidente_id
  missao.delete()
  return index2(request, acidenteId)

def index2(request, acidenteId):
  acidente = Acidente.objects.get(id=acidenteId)
  missoes = acidente.missao_set.all()
  return render(request, 'missoes/index.html', {'acidente': acidente, 'missoes': missoes})
