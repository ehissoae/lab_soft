from django.shortcuts import render
from recursos.models import Recurso

# Create your views here.
def index(request):
  recursos = Recurso.objects.all()
  tipoAcesso = request.user.profile.tipoAcesso
  return render(request, 'recursos/index.html', {"tipoAcesso":tipoAcesso, 'recursos': recursos})
