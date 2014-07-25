from django.http import HttpResponse
from django.shortcuts import render
from SiGeCAV.utils import *

# Create your views here.
def index(request):
	url = url_if_not_authenticated(request)
	if(url):
		return url
		
	tipoAcesso = request.user.profile.tipoAcesso
	return render(request, 'recursos/index.html', {"tipoAcesso":tipoAcesso})

