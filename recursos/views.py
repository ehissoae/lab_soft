from django.http import HttpResponse
from django.shortcuts import render
from SiGeCAV.utils import *

# Create your views here.
def index(request):
	redirect = url_if_not_authenticated(request)
	if(redirect):
		return redirect
		
	tipoAcesso = request.user.profile.tipoAcesso
	return render(request, 'recursos/index.html', {"tipoAcesso":tipoAcesso})

