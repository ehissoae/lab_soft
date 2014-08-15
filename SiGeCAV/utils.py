from django.shortcuts import render, redirect
from django.contrib.auth.views import login
from django.conf import settings
from django.http import Http404

def url_if_not_authenticated(request):
  if not request.user.is_authenticated():
    return login(request)

def url_if_not_coordenador(request):
  if not request.user.is_authenticated():
    return login(request)
  if request.user.profile.tipoAcesso != 'coordenador':
    raise Http404

def url_if_not_especialista(request):
  if not request.user.is_authenticated():
    return login(request)
  if request.user.profile.tipoAcesso != 'especialista':
    raise Http404

def url_if_not_administrador(request):
  if not request.user.is_authenticated():
    return login(request)
  if request.user.profile.tipoAcesso != 'administrador':
    raise Http404