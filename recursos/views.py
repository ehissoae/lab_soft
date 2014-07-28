from django.shortcuts import render
from recursos.models import Recurso

# Create your views here.
def index(request):
<<<<<<< HEAD
  recursos = Recurso.objects.all()
  return render(request, 'recursos/index.html', {'recursos': recursos})
=======
	tipoAcesso = request.user.profile.tipoAcesso
	return render(request, 'recursos/index.html', {"tipoAcesso":tipoAcesso})

>>>>>>> cca927fdbfd5461583d2610e6cf611599bd02163
