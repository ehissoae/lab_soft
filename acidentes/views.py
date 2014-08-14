from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
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
    if dataHora and local and descricao:
      dataHora = datetime.strptime(dataHora, '%d/%m/%Y %H:%M')
      acidente = Acidente.objects.create(dataHora=dataHora, local=local, descricao=descricao)
      acidente.coordenador = request.user
      acidente.save()
      return redirect(acidente)
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
    acidente.save()
    return redirect(acidente)

def delete(request):
  acidenteId = request.GET.get("id", "")
  Acidente.objects.get(id=acidenteId).delete()
  return redirect('acidentes')