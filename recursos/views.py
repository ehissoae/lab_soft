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
  return render(request, 'recursos/index.html', {'recursos': recursos, "tipoAcesso":tipoAcesso})
