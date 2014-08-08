from django.shortcuts import render
from acidentes.models import Acidente
from datetime import datetime

# Create your views here.
def index(request):
  acidentes = Acidente.objects.all()
  return render(request, 'acidentes/index.html', {'acidentes': acidentes})

def detail(request):
  acidenteId = request.GET.get("id", "")
  acidente = Acidente.objects.get(id=acidenteId)
  return render(request, 'acidentes/detalhes.html', {'acidente': acidente})

def new(request):
  if request.method == "GET":
    return render(request, 'acidentes/novo.html', {})
  elif request.method == "POST":
    dataHora = request.POST.get("dataHora", "")
    local = request.POST.get("local", "")
    descricao = request.POST.get("descricao", "")
    SVCid = request.POST.get("SVCid", "")
    if dataHora and local and descricao and SVCid:
      dataHora = datetime.strptime(dataHora, '%d/%m/%Y %H:%M')
      Acidente.objects.create(dataHora=dataHora, local=local, SVCid=SVCid, descricao=descricao)
      return index(request)
    return render(request, 'acidentes/novo.html', {})

def edit(request):
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
    return render(request, 'acidentes/detalhes.html', {'acidente': acidente})

def delete(request):
  acidenteId = request.GET.get("id", "")
  Acidente.objects.get(id=acidenteId).delete()
  return index(request)