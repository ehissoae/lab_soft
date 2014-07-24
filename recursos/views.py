from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	tipoAcesso = request.user.profile.tipoAcesso
	return render(request, 'recursos/index.html', {"tipoAcesso":tipoAcesso})

