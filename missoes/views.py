from django.shortcuts import render, redirect
from missoes.models import Missao, AlocacaoRecurso
from recursos.models import Recurso
from acidentes.models import Acidente
from django.db.models import Q

# Create your views here.
def index(request):
  acidenteId = request.GET.get("acidente_id", "")
  acidente = Acidente.objects.get(id=acidenteId)
  missoes = acidente.missao_set.exclude(status="removido")
  return render(request, 'missoes/index.html', {
    'acidente': acidente, 
    'missoes': missoes,
    'mission_types': Missao.MISSION_TYPES,
  })

def detail(request):
  missaoId = request.GET.get("id", "")
  missao = Missao.objects.get(id=missaoId)
  alocacoesRecurso = AlocacaoRecurso.objects.filter(missao_id=missao.id)
  return render(request, 'missoes/detalhes.html', {'missao': missao, 'alocacoesRecurso': alocacoesRecurso})

def new(request):
  if request.method == "GET":
    acidenteId = request.GET.get("acidente_id", "")
    acidente = Acidente.objects.get(id=acidenteId)
    return render(request, 'missoes/novo.html', {
      'acidente':acidente,
      'mission_types': Missao.MISSION_TYPES,
    })
  elif request.method == "POST":
    nome = request.POST.get("nome", "")
    tipoMissao = request.POST.get("tipoMissao", "")
    acidenteId = request.POST.get("acidente_id", "")
    if nome and tipoMissao and acidenteId:
      acidente = Acidente.objects.get(id=acidenteId)
      missao = Missao.objects.create(nome=nome, tipoMissao=tipoMissao, acidente_id=acidenteId)

      if acidente.especialista == None:
        acidente.especialista = request.user
        acidente.save()

      if acidente.status == 'aguardandoAnalise':
        acidente.status = 'emAndamento'
        acidente.save()

      return redirect(missao)
    return render(request, 'missoes/novo.html', {})

def changeStatus(request):
  if request.method == "GET":
    missaoId = request.GET.get("id", "")
    missao = Missao.objects.get(id=missaoId)
    return render(request, 'missoes/alterarStatus.html', {
      'missao': missao,
      'statuses_types': Missao.STATUSES_TYPES,
      })
  elif request.method == "POST":
    missaoId = request.GET.get("id", "")
    missao = Missao.objects.get(id=missaoId)
    missao.status = request.POST.get("status", "")
    missao.save()
    allMissionsCompleted = missao.acidente.missao_set.filter(Q(status="aguardandoRecursos") | Q(status="emAndamento")).count() == 0
    if allMissionsCompleted:
      acidente = missao.acidente
      acidente.status = "finalizado"
      acidente.save()
    return redirect(missao)

def delete(request):
  missaoId = request.GET.get("id", "")
  missao = Missao.objects.get(id=missaoId)
  acidenteId = missao.acidente_id
  missao.status = "removido"
  AlocacaoRecurso.objects.filter(missao_id=missaoId).delete()
  missao.save()
  return redirect('/acidentes/missoes?acidente_id=' + str(acidenteId))

def assignResource(request):
  recursos = Recurso.objects.exclude(status="removido")
  if request.method == "GET":
    acidenteId = request.GET.get("acidente_id", "")
    acidente = Acidente.objects.get(id=acidenteId)

    missaoId = request.GET.get("missao_id", "")
    missao = Missao.objects.get(id=missaoId)

    return render(request, 'missoes/alocarRecurso.html', {'acidente':acidente, 'missao':missao, 'recursos':recursos})
  elif request.method == "POST":
    quantidadeAlocada = request.POST.get("quantidadeAlocada", 0)
    observacao = request.POST.get("observacao", "")
    recursoId = request.POST.get("recurso_id", "")
    missaoId = request.POST.get("missao_id", "")
    another_one = request.POST.get("continue", "")
    missao = Missao.objects.get(id=missaoId)

    if recursoId and missaoId:
      AlocacaoRecurso.objects.create(recurso_id=recursoId, missao_id=missaoId, quantidadeAlocada=quantidadeAlocada, observacao=observacao)
      if not another_one:
        return redirect(missao)
    missao = Missao.objects.get(id=missaoId)
    acidente = missao.acidente
    return render(request, 'missoes/alocarRecurso.html', {'acidente':acidente, 'missao':missao, 'recursos':recursos})

def assignedResourceDetails(request):
  recursoAlocadoId = request.GET.get("id", "")
  recursoAlocado = AlocacaoRecurso.objects.get(id=recursoAlocadoId)
  return render(request, 'missoes/detalhesRecursoAlocado.html', {'recursoAlocado': recursoAlocado})

def deleteAssignedResource(request):
  alocacaoRecursoId = request.GET.get("id", "")
  alocacaoRecurso = AlocacaoRecurso.objects.get(id=alocacaoRecursoId)
  missao = alocacaoRecurso.missao
  alocacaoRecurso.delete()
  return redirect(missao)
